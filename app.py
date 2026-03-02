import streamlit as st
import plotly.graph_objects as go
import numpy as np

from utils.calculations import (
    haversine,
    calculate_flight,
    great_circle_points,
    calculate_operational_risk
)
from utils.airports import airports, airport_display_list, display_to_icao
from utils.aircraft_data import aircraft_database
from utils.pdf_export import generate_pdf

st.set_page_config(page_title="SkyRoute PRO", layout="wide")

# ===============================
# DARK UI
# ===============================
st.markdown("""
<style>
.stApp { background-color: #0A192F; color: #E6F1FF; }
h1 { color: #64FFDA; }
</style>
""", unsafe_allow_html=True)

st.title("✈️ SkyRoute PRO – Aviation Intelligence")

# ===============================
# CATEGORY FILTER
# ===============================
categories = sorted(set(a["category"] for a in aircraft_database.values()))
selected_category = st.selectbox("Aircraft Category", categories)

filtered_aircraft = [
    name for name, data in aircraft_database.items()
    if data["category"] == selected_category
]

# ===============================
# INPUT SECTION
# ===============================
col1, col2 = st.columns(2)

with col1:
    departure_display = st.selectbox("Departure", airport_display_list)
    destination_display = st.selectbox("Destination", airport_display_list)

with col2:
    aircraft = st.selectbox("Aircraft", sorted(filtered_aircraft))
    altitude = st.slider("Cruise Altitude", 20000, 45000, 35000)
    fuel_price = st.number_input("Fuel Price per kg", 0.5, 5.0, 1.2)

# ===============================
# SESSION STATE
# ===============================
if "analysis_data" not in st.session_state:
    st.session_state.analysis_data = None

if st.button("Analyze Flight"):
    dep = airports[display_to_icao[departure_display]]
    dest = airports[display_to_icao[destination_display]]
    distance = haversine(dep["lat"], dep["lon"], dest["lat"], dest["lon"])
    result = calculate_flight(distance, aircraft, altitude, fuel_price)

    st.session_state.analysis_data = {
        "dep": dep,
        "dest": dest,
        "distance": distance,
        "result": result,
        "aircraft": aircraft,
        "altitude": altitude,
        "fuel_price": fuel_price
    }

# ===============================
# SHOW RESULTS
# ===============================
if st.session_state.analysis_data:

    data = st.session_state.analysis_data
    dep = data["dep"]
    dest = data["dest"]
    distance = data["distance"]
    result = data["result"]
    aircraft = data["aircraft"]
    altitude = data["altitude"]
    fuel_price = data["fuel_price"]

    # -------------------------------
    # Core Metrics
    # -------------------------------
    st.subheader("📊 Core Metrics")

    a, b, c = st.columns(3)
    a.metric("Distance (km)", round(distance, 2))
    b.metric("Fuel (kg)", result["total_fuel"])
    c.metric("Cost", result["total_cost"])

    if result["range_warning"]:
        st.error("⚠️ Route exceeds aircraft maximum range.")

    # -------------------------------
    # Operational Risk
    # -------------------------------
    st.subheader("🧠 Operational Risk Assessment")

    risk_score, risk_breakdown = calculate_operational_risk(
        distance,
        aircraft,
        altitude,
        result["wind_factor"]
    )

    if risk_score < 35:
        level = "Low Risk"
        color = "green"
    elif risk_score < 65:
        level = "Moderate Risk"
        color = "orange"
    else:
        level = "High Risk"
        color = "red"

    st.markdown(f"### Risk Score: {risk_score}/100")
    st.markdown(
        f"<span style='color:{color}; font-size:20px;'>● {level}</span>",
        unsafe_allow_html=True
    )

    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=risk_score,
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "#64FFDA"},
            "steps": [
                {"range": [0, 35], "color": "green"},
                {"range": [35, 65], "color": "orange"},
                {"range": [65, 100], "color": "red"},
            ],
        },
    ))

    fig_gauge.update_layout(height=350)
    st.plotly_chart(fig_gauge, use_container_width=True)

    fig_risk = go.Figure()
    fig_risk.add_trace(go.Bar(
        x=list(risk_breakdown.keys()),
        y=list(risk_breakdown.values())
    ))
    fig_risk.update_layout(height=350)
    st.plotly_chart(fig_risk, use_container_width=True)

    # -------------------------------
    # Mission Feasibility
    # -------------------------------
    st.subheader("📊 Mission Feasibility Analysis")

    aircraft_data = aircraft_database[aircraft]
    max_range = aircraft_data["max_range"]

    range_utilization = (distance / max_range) * 100

    if range_utilization <= 60:
        mission_status = "Ideal Mission"
        mission_color = "green"
    elif range_utilization <= 85:
        mission_status = "High Utilization"
        mission_color = "orange"
    elif range_utilization <= 100:
        mission_status = "Near Operational Limit"
        mission_color = "red"
    else:
        mission_status = "Mission Not Feasible"
        mission_color = "darkred"

    st.markdown(f"### Range Utilization: {round(range_utilization,2)}%")
    st.markdown(
        f"<span style='color:{mission_color}; font-size:20px;'>● {mission_status}</span>",
        unsafe_allow_html=True
    )

    fig_range = go.Figure(go.Indicator(
        mode="gauge+number",
        value=range_utilization,
        gauge={
            "axis": {"range": [0, 120]},
            "bar": {"color": "#64FFDA"},
            "steps": [
                {"range": [0, 60], "color": "green"},
                {"range": [60, 85], "color": "orange"},
                {"range": [85, 100], "color": "red"},
                {"range": [100, 120], "color": "darkred"},
            ],
        },
    ))

    fig_range.update_layout(height=350)
    st.plotly_chart(fig_range, use_container_width=True)

    # -------------------------------
    # Route Map
    # -------------------------------
    st.subheader("🌍 Flight Route")

    lat_curve, lon_curve = great_circle_points(
        dep["lat"], dep["lon"],
        dest["lat"], dest["lon"]
    )

    fig = go.Figure()

    fig.add_trace(go.Scattergeo(
        lon=lon_curve,
        lat=lat_curve,
        mode="lines",
        line=dict(width=2, color="#64FFDA"),
        name="Route"
    ))

    fig.add_trace(go.Scattergeo(
        lon=[dep["lon"], dest["lon"]],
        lat=[dep["lat"], dest["lat"]],
        mode="markers",
        marker=dict(size=8, color="red"),
        name="Airports"
    ))

    fig.update_layout(
        geo=dict(
            projection_type="natural earth",
            showland=True,
            landcolor="rgb(20,30,50)",
            bgcolor="#0A192F",
            showcountries=True
        ),
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

    # -------------------------------
    # Fleet Comparison
    # -------------------------------
    st.subheader("🛩 Fleet Comparison")

    fleet_selection = st.multiselect(
        "Select Aircraft for Fleet Comparison",
        sorted(filtered_aircraft),
        key="fleet_compare"
    )

    if fleet_selection:
        fig_comp = go.Figure()

        for ac in fleet_selection:
            r = calculate_flight(distance, ac, altitude, fuel_price)
            fig_comp.add_trace(go.Bar(
                name=ac,
                x=["Fuel (kg)"],
                y=[r["total_fuel"]]
            ))

        fig_comp.update_layout(barmode="group")
        st.plotly_chart(fig_comp, use_container_width=True)

        # -------------------------------
    # Export PDF
    # -------------------------------
    st.subheader("📄 Export Report")

    report_data = {
        "aircraft": aircraft,
        "departure": departure_display,
        "destination": destination_display,
        "distance": round(distance, 2),
        "altitude": altitude,
        "fuel": result["total_fuel"],
        "cost": result["total_cost"],
        "co2": result["co2"],
        "risk_score": risk_score,
        "risk_level": level,
        "range_utilization": round(range_utilization, 2),
        "mission_status": mission_status
    }

    generate_pdf("skyroute_report.pdf", report_data)

    with open("skyroute_report.pdf", "rb") as f:
        st.download_button(
            "Download Full Analysis Report",
            f,
            "SkyRoute_Full_Report.pdf"
        )