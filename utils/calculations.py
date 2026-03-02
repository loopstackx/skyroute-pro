import math
import random
import numpy as np
from .aircraft_data import aircraft_database


def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = (math.sin(dlat/2)**2 +
         math.cos(math.radians(lat1)) *
         math.cos(math.radians(lat2)) *
         math.sin(dlon/2)**2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c


def great_circle_points(lat1, lon1, lat2, lon2, num_points=100):

    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])

    d = 2 * np.arcsin(
        np.sqrt(
            np.sin((lat2 - lat1) / 2) ** 2 +
            np.cos(lat1) * np.cos(lat2) *
            np.sin((lon2 - lon1) / 2) ** 2
        )
    )

    f = np.linspace(0, 1, num_points)

    A = np.sin((1 - f) * d) / np.sin(d)
    B = np.sin(f * d) / np.sin(d)

    x = A * np.cos(lat1) * np.cos(lon1) + B * np.cos(lat2) * np.cos(lon2)
    y = A * np.cos(lat1) * np.sin(lon1) + B * np.cos(lat2) * np.sin(lon2)
    z = A * np.sin(lat1) + B * np.sin(lat2)

    lat_points = np.degrees(np.arctan2(z, np.sqrt(x ** 2 + y ** 2)))
    lon_points = np.degrees(np.arctan2(y, x))

    return lat_points, lon_points


def calculate_flight(distance_km, aircraft, altitude, fuel_price):

    data = aircraft_database[aircraft]

    speed = data["speed"]
    fuel_burn_hr = data["fuel_burn"]
    passengers = data["passengers"]
    optimal_alt = data["optimal_altitude"]

    flight_time = distance_km / speed
    base_fuel = fuel_burn_hr * flight_time

    # Wind
    wind_factor = random.uniform(-0.05, 0.08)
    wind_adjustment = base_fuel * wind_factor
    fuel_after_wind = base_fuel + wind_adjustment

    # Altitude penalty
    alt_diff = abs(altitude - optimal_alt)
    altitude_penalty = fuel_after_wind * ((alt_diff / 10000) * 0.03)

    total_fuel = fuel_after_wind + altitude_penalty

    # Sustainability
    co2 = total_fuel * 3.16
    total_cost = total_fuel * fuel_price

    return {
        "flight_time": round(flight_time, 2),
        "total_fuel": round(total_fuel, 2),
        "base_fuel": round(base_fuel, 2),
        "wind_adjustment": round(wind_adjustment, 2),
        "altitude_penalty": round(altitude_penalty, 2),
        "co2": round(co2, 2),
        "total_cost": round(total_cost, 2),
        "passengers": passengers,
        "range_warning": distance_km > data["max_range"],
        "wind_factor": wind_factor   # IMPORTANT FOR RISK
    }

def calculate_operational_risk(distance_km, aircraft, altitude, wind_factor):

    data = aircraft_database[aircraft]

    # 1️⃣ Distance factor
    distance_risk = min(distance_km / 15000, 1) * 25

    # 2️⃣ Range utilization
    range_utilization = distance_km / data["max_range"]
    range_risk = min(range_utilization, 1) * 25

    # 3️⃣ Altitude deviation
    alt_diff = abs(altitude - data["optimal_altitude"])
    altitude_risk = min(alt_diff / 15000, 1) * 20

    # 4️⃣ Wind impact
    wind_risk = min(abs(wind_factor) * 100 * 0.3, 20)

    # 5️⃣ Aircraft category base risk
    category_weights = {
        "Turboprop": 10,
        "Regional": 8,
        "Narrowbody": 6,
        "Widebody": 5,
        "Private": 7
    }

    category_risk = category_weights.get(data["category"], 5)

    total_risk = (
        distance_risk +
        range_risk +
        altitude_risk +
        wind_risk +
        category_risk
    )

    total_risk = min(total_risk, 100)

    breakdown = {
        "Distance": round(distance_risk, 2),
        "Range": round(range_risk, 2),
        "Altitude": round(altitude_risk, 2),
        "Wind": round(wind_risk, 2),
        "Aircraft": category_risk
    }

    return round(total_risk, 2), breakdown

def calculate_operational_risk(distance_km, aircraft, altitude, wind_factor):

    data = aircraft_database[aircraft]

    # Distance risk (long-haul fatigue / ops complexity)
    distance_risk = min(distance_km / 15000, 1) * 25

    # Range utilization risk
    range_utilization = distance_km / data["max_range"]
    range_risk = min(range_utilization, 1) * 25

    # Altitude deviation risk
    alt_diff = abs(altitude - data["optimal_altitude"])
    altitude_risk = min(alt_diff / 15000, 1) * 20

    # Wind variability risk
    wind_risk = abs(wind_factor) * 100 * 0.2

    # Aircraft category base risk
    category_weights = {
        "Turboprop": 10,
        "Regional": 8,
        "Narrowbody": 6,
        "Widebody": 5,
        "Private": 7
    }

    category_risk = category_weights.get(data["category"], 5)

    total_risk = distance_risk + range_risk + altitude_risk + wind_risk + category_risk

    total_risk = min(total_risk, 100)

    return round(total_risk, 2), {
        "Distance": round(distance_risk, 2),
        "Range Utilization": round(range_risk, 2),
        "Altitude Deviation": round(altitude_risk, 2),
        "Wind": round(wind_risk, 2),
        "Aircraft Type": category_risk
    }