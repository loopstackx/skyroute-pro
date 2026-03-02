from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle


def generate_pdf(filename, report):

    doc = SimpleDocTemplate(filename)
    elements = []

    styles = getSampleStyleSheet()
    style = styles["Normal"]

    # Title
    elements.append(Paragraph("<b>SkyRoute PRO - Flight Analysis Report</b>", styles["Title"]))
    elements.append(Spacer(1, 0.3 * inch))

    # Section 1 - Flight Info
    elements.append(Paragraph("<b>Flight Overview</b>", styles["Heading2"]))
    elements.append(Spacer(1, 0.2 * inch))

    flight_data = [
        ["Aircraft", report["aircraft"]],
        ["Departure", report["departure"]],
        ["Destination", report["destination"]],
        ["Distance (km)", report["distance"]],
        ["Cruise Altitude (ft)", report["altitude"]],
    ]

    t1 = Table(flight_data)
    t1.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey)
    ]))

    elements.append(t1)
    elements.append(Spacer(1, 0.4 * inch))

    # Section 2 - Performance
    elements.append(Paragraph("<b>Performance Metrics</b>", styles["Heading2"]))
    elements.append(Spacer(1, 0.2 * inch))

    perf_data = [
        ["Total Fuel (kg)", report["fuel"]],
        ["Total Cost", report["cost"]],
        ["Total CO2 (kg)", report["co2"]],
    ]

    t2 = Table(perf_data)
    t2.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey)
    ]))

    elements.append(t2)
    elements.append(Spacer(1, 0.4 * inch))

    # Section 3 - Risk
    elements.append(Paragraph("<b>Operational Risk</b>", styles["Heading2"]))
    elements.append(Spacer(1, 0.2 * inch))

    risk_data = [
        ["Risk Score", report["risk_score"]],
        ["Risk Level", report["risk_level"]],
    ]

    t3 = Table(risk_data)
    t3.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey)
    ]))

    elements.append(t3)
    elements.append(Spacer(1, 0.4 * inch))

    # Section 4 - Mission
    elements.append(Paragraph("<b>Mission Feasibility</b>", styles["Heading2"]))
    elements.append(Spacer(1, 0.2 * inch))

    mission_data = [
        ["Range Utilization (%)", report["range_utilization"]],
        ["Mission Status", report["mission_status"]],
    ]

    t4 = Table(mission_data)
    t4.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey)
    ]))

    elements.append(t4)

    doc.build(elements)