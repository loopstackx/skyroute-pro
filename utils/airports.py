import pandas as pd
import os

CSV_PATH = os.path.join("data", "airports.csv")

# OpenFlights format columns (no header in file)
columns = [
    "AirportID",
    "Name",
    "City",
    "Country",
    "IATA",
    "ICAO",
    "Latitude",
    "Longitude",
    "Altitude",
    "Timezone",
    "DST",
    "Tz",
    "Type",
    "Source"
]

# Load CSV WITHOUT header
df = pd.read_csv(CSV_PATH, header=None, names=columns)

# Keep only valid ICAO codes
df = df[df["ICAO"].notnull()]
df = df[df["ICAO"] != "\\N"]

# Keep required columns
df = df[["ICAO", "Name", "Latitude", "Longitude"]]

# Clean ICAO
df["ICAO"] = df["ICAO"].astype(str).str.strip().str.upper()

# Remove duplicates
df = df.drop_duplicates(subset="ICAO")

# Create display label
df["display"] = df["Name"] + " (" + df["ICAO"] + ")"

# Dictionary for calculations
airports = {
    row["ICAO"]: {
        "name": row["Name"],
        "lat": float(row["Latitude"]),
        "lon": float(row["Longitude"])
    }
    for _, row in df.iterrows()
}

# For dropdown
airport_display_list = sorted(df["display"].tolist())

display_to_icao = {
    row["display"]: row["ICAO"]
    for _, row in df.iterrows()
}

print(f"Loaded {len(airports)} airports successfully.")