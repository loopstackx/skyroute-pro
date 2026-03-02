# utils/aircraft_data.py

aircraft_database = {

# ===============================
# Airbus Narrowbody
# ===============================
"A220-100": {"fuel_burn": 2100, "speed": 830, "max_range": 6300, "passengers": 120, "optimal_altitude": 35000, "category": "Narrowbody"},
"A220-300": {"fuel_burn": 2300, "speed": 830, "max_range": 6200, "passengers": 145, "optimal_altitude": 35000, "category": "Narrowbody"},
"A318": {"fuel_burn": 2400, "speed": 830, "max_range": 5700, "passengers": 132, "optimal_altitude": 35000, "category": "Narrowbody"},
"A319": {"fuel_burn": 2500, "speed": 830, "max_range": 6900, "passengers": 156, "optimal_altitude": 35000, "category": "Narrowbody"},
"A320": {"fuel_burn": 2600, "speed": 830, "max_range": 6100, "passengers": 180, "optimal_altitude": 35000, "category": "Narrowbody"},
"A321": {"fuel_burn": 2900, "speed": 840, "max_range": 7400, "passengers": 220, "optimal_altitude": 36000, "category": "Narrowbody"},
"A321neo": {"fuel_burn": 2600, "speed": 840, "max_range": 8700, "passengers": 220, "optimal_altitude": 36000, "category": "Narrowbody"},

# ===============================
# Boeing Narrowbody
# ===============================
"B737-700": {"fuel_burn": 2400, "speed": 820, "max_range": 5500, "passengers": 149, "optimal_altitude": 35000, "category": "Narrowbody"},
"B737-800": {"fuel_burn": 2600, "speed": 830, "max_range": 5700, "passengers": 189, "optimal_altitude": 35000, "category": "Narrowbody"},
"B737-900": {"fuel_burn": 2800, "speed": 830, "max_range": 5900, "passengers": 220, "optimal_altitude": 36000, "category": "Narrowbody"},
"B737 MAX 8": {"fuel_burn": 2400, "speed": 840, "max_range": 6500, "passengers": 178, "optimal_altitude": 36000, "category": "Narrowbody"},
"B737 MAX 9": {"fuel_burn": 2600, "speed": 840, "max_range": 6500, "passengers": 193, "optimal_altitude": 36000, "category": "Narrowbody"},
"B737 MAX 10": {"fuel_burn": 2800, "speed": 840, "max_range": 6100, "passengers": 230, "optimal_altitude": 36000, "category": "Narrowbody"},

# ===============================
# Regional Jets
# ===============================
"E170": {"fuel_burn": 1700, "speed": 810, "max_range": 3900, "passengers": 80, "optimal_altitude": 33000, "category": "Regional"},
"E175": {"fuel_burn": 1800, "speed": 820, "max_range": 4000, "passengers": 88, "optimal_altitude": 33000, "category": "Regional"},
"E190": {"fuel_burn": 2100, "speed": 830, "max_range": 4500, "passengers": 100, "optimal_altitude": 33000, "category": "Regional"},
"E195": {"fuel_burn": 2200, "speed": 830, "max_range": 4800, "passengers": 120, "optimal_altitude": 34000, "category": "Regional"},
"CRJ700": {"fuel_burn": 1700, "speed": 810, "max_range": 3700, "passengers": 78, "optimal_altitude": 33000, "category": "Regional"},
"CRJ900": {"fuel_burn": 1900, "speed": 820, "max_range": 4500, "passengers": 90, "optimal_altitude": 33000, "category": "Regional"},
"CRJ1000": {"fuel_burn": 2100, "speed": 820, "max_range": 4600, "passengers": 100, "optimal_altitude": 34000, "category": "Regional"},

# ===============================
# Turboprops
# ===============================
"ATR 42": {"fuel_burn": 800, "speed": 500, "max_range": 1500, "passengers": 48, "optimal_altitude": 25000, "category": "Turboprop"},
"ATR 72": {"fuel_burn": 900, "speed": 510, "max_range": 1600, "passengers": 78, "optimal_altitude": 25000, "category": "Turboprop"},
"Dash 8 Q400": {"fuel_burn": 1000, "speed": 550, "max_range": 2000, "passengers": 82, "optimal_altitude": 25000, "category": "Turboprop"},

# ===============================
# Widebody Airbus
# ===============================
"A330-200": {"fuel_burn": 5800, "speed": 860, "max_range": 13400, "passengers": 247, "optimal_altitude": 39000, "category": "Widebody"},
"A330-300": {"fuel_burn": 6200, "speed": 860, "max_range": 11700, "passengers": 300, "optimal_altitude": 39000, "category": "Widebody"},
"A350-900": {"fuel_burn": 6000, "speed": 900, "max_range": 15000, "passengers": 325, "optimal_altitude": 39000, "category": "Widebody"},
"A350-1000": {"fuel_burn": 6500, "speed": 900, "max_range": 16000, "passengers": 366, "optimal_altitude": 40000, "category": "Widebody"},
"A380": {"fuel_burn": 11500, "speed": 900, "max_range": 15200, "passengers": 555, "optimal_altitude": 41000, "category": "Widebody"},

# ===============================
# Widebody Boeing
# ===============================
"B767-300": {"fuel_burn": 5500, "speed": 850, "max_range": 9700, "passengers": 218, "optimal_altitude": 39000, "category": "Widebody"},
"B777-200": {"fuel_burn": 7000, "speed": 905, "max_range": 9700, "passengers": 314, "optimal_altitude": 39000, "category": "Widebody"},
"B777-300ER": {"fuel_burn": 7500, "speed": 905, "max_range": 13600, "passengers": 396, "optimal_altitude": 39000, "category": "Widebody"},
"B787-8": {"fuel_burn": 5400, "speed": 900, "max_range": 13600, "passengers": 242, "optimal_altitude": 40000, "category": "Widebody"},
"B787-9": {"fuel_burn": 5600, "speed": 900, "max_range": 14100, "passengers": 290, "optimal_altitude": 40000, "category": "Widebody"},
"B787-10": {"fuel_burn": 6000, "speed": 900, "max_range": 11900, "passengers": 330, "optimal_altitude": 41000, "category": "Widebody"},

# ===============================
# Private Jets
# ===============================
"Cessna Citation CJ3": {"fuel_burn": 600, "speed": 770, "max_range": 3700, "passengers": 9, "optimal_altitude": 41000, "category": "Private"},
"Cessna Citation X": {"fuel_burn": 900, "speed": 970, "max_range": 6000, "passengers": 12, "optimal_altitude": 43000, "category": "Private"},
"Gulfstream G550": {"fuel_burn": 1300, "speed": 900, "max_range": 12500, "passengers": 19, "optimal_altitude": 43000, "category": "Private"},
"Gulfstream G650": {"fuel_burn": 1400, "speed": 956, "max_range": 13000, "passengers": 19, "optimal_altitude": 45000, "category": "Private"},
"Bombardier Global 6000": {"fuel_burn": 1350, "speed": 900, "max_range": 11100, "passengers": 17, "optimal_altitude": 43000, "category": "Private"},
"Bombardier Global 7500": {"fuel_burn": 1500, "speed": 910, "max_range": 14200, "passengers": 19, "optimal_altitude": 45000, "category": "Private"},
"Dassault Falcon 7X": {"fuel_burn": 1200, "speed": 900, "max_range": 11000, "passengers": 16, "optimal_altitude": 43000, "category": "Private"},
"Dassault Falcon 8X": {"fuel_burn": 1300, "speed": 900, "max_range": 11900, "passengers": 16, "optimal_altitude": 43000, "category": "Private"}
}