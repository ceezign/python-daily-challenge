# Working Weather Simulator
# shows 7 days demo for multiple cities

import random
from datetime import datetime, timedelta


# utility function
def c_to_f(c): return c * 9/5 + 32
def f_to_c(f): return (f - 32) * 5/9

def heat_index_c(temp_c, rh):
    """ Approximate heat index in Celsius using conversion to fahrenheit and Rothfusz regression.
    returns feels-like temp in Celsius
    """

    T = c_to_f(temp_c)
    R = rh
    # Rothfusz regression (valid for T >= 80F and RH >= 40%)
    HI = -42.379 + 2.04901523 * T + 10.14333127 * R - 0.22475541 * T * R \
         - 0.00683783 * T * T - 0.05481717 * R * R + 0.00122874 * T * T * R \
         + 0.00085282 * T * R * R - 0.00000199 * T * T * R * R
    # adjustment for some RH/Temp ranges (simple)
    if R < 13 and 80 <= T <= 112:
        HI -= ((13 - R) / 4) * ((17 - abs(T - 95)) / 17)
    elif R > 85 and 80 <= T <= 87:
        HI += ((R - 85) / 10) * ((87 - T) / 5)
    return f_to_c(HI) if T >= 80 and R >= 40 else temp_c

def wind_chill_c(temp_c, wind_kmh):
    """wind chill formula (anadian) - returns feels-like in celsius.
    valid for temperature <=10degreeC and wind speed >4.8 km/h"""
    v = wind_kmh
    t = temp_c
    if t > 10 or v < 4.8:
        return temp_c
    wc = 13.12 + 0.6215 * t - 11.37 * (v**0.16) + 0.3965 * t * (v**0.16)
    return wc

#  Weather Models
CONDITIONS = [
    ("Sunny", "☀️"),
    ("Partly Cloudy", "⛅"),
    ("Cloudy", "☁️"),
    ("Light Rain", "🌦️"),
    ("Rain", "🌧️"),
    ("Storm", "⛈️"),
    ("Drizzle", "🌦️"),
    ("Snow", "❄️"),
    ("Sleet", "🌨️"),
    ("Fog", "🌫️"),
]

SEASON_BASES = {
    "winter":    {"temp_mean": 5,   "temp_var": 6,  "rain_chance": 30, "wind_mean": 15},
    "spring":    {"temp_mean": 15,  "temp_var": 8,  "rain_chance": 40, "wind_mean": 12},
    "summer":    {"temp_mean": 28,  "temp_var": 6,  "rain_chance": 35, "wind_mean": 10},
    "fall":      {"temp_mean": 12,  "temp_var": 7,  "rain_chance": 45, "wind_mean": 14},
}

CITY_PROFILES = {
    "Lagos": {"season_shift": {"winter": 5, "spring": 3, "summer": 2, "fall": 4}},
    "London": {"season_shift": {"winter": -2, "spring": 0, "summer": 2, "fall": 0}},
    "New York": {"season_shift": {"winter": -5, "spring": 0, "summer": 3, "fall": -1}},
    "Tokyo": {"season_shift": {"winter": -1, "spring": 1, "summer": 4, "fall": 0}},
}

def pick_condition(rain_chance):
    roll = random.randint(1, 100)
    if roll <= rain_chance // 2:
        return random.choice([c for c in CONDITIONS if "Rain" in c[0] or
                              c[0] in ("Drizzle", "Storm")])

    if roll <= rain_chance:
        return random.choice([c for c in CONDITIONS if "Cloud" in c[0] or
                              "Drizzle" in c[0] or "fog" in c[0] ])

    if random.random() < 0.05:
        return ("Storm", "⛈️")
    return random.choice([c for c in CONDITIONS if c[0] in
                          ("Sunny", "Partly Cloudy", "Cloudy")])

def generate_daily_weather(city, season):
    base = SEASON_BASES.get(season.lower())
    shift = CITY_PROFILES.get(city, {}).get("season_shift", {}).get(season, 0)
    mean = base["temp_mean"] + shift
    temp = round(random.gauss(mean, base["temp_var"]), 1)
    humidity = max(10, min(100, int(random.gauss(60, 20) )))
    wind = max(0, round(random.gauss(base["wind_mean"], 6), 1))
    rain_chance = min(95, max(0, base["rain_chance"] + int((humidity-50) / 5)))
    condition, emoji = pick_condition(rain_chance)
    precipitation_mm = 0.0
    if "Rain" in condition or "Drizzle" in condition or condition == "Storm":
        precipitation_mm = round(max(0, random.gauss(5 + humidity/10, 8)), 1)

    if condition == "Storm":
        wind = max(wind, random.uniform(25, 90))

    feels_like = wind_chill_c(temp, wind)
    feels_like = heat_index_c(feels_like, humidity)
    warning = None
    if temp >= 40 or feels_like >= 45:
        warning = "Extreme heat warning"
    elif temp <= -10 or feels_like <= -20:
        warning = "Extreme cold warning"
    elif wind >= 80:
        warning = "High wind warning"
    elif precipitation_mm > 50:
        warning = "Heavy precipitation warning"

    return  {
        "city": city,
        "date": None,
        "season": season.title(),
        "temp_c": temp,
        "feels_like_c": round(feels_like, 1),
        "humidity": humidity,
        "wind_kmh": round(wind, 1),
        "condition": condition,
        "emoji": emoji,
        "precip_mm": precipitation_mm,
        "rain_chance_pct": rain_chance,
        "warning": warning,

    }

def generate_forecast(city, season, start_date, days=7):
    history = []
    for i in range(days):
        day = start_date + timedelta(days=i)
        entry = generate_daily_weather(city, season)
        entry["date"] = day.strftime("%Y-%m-%d (%a)")
        history.append(entry)
    return history

def summarize_history(history):
    temps = [h["temp_c"] for h in history]
    feels = [h["feels_like_c"] for h in history]
    winds = [h["wind_kmh"] for h in history]
    hums = [h["humidity"] for h in history]
    avg = {
        "avg_temp": round(sum(temps)/len(temps), 1),
        "avg_feels_like": round(sum(feels)/len(feels), 1),
        "max_temp": max(temps),
        "min_temp": min(temps),
        "max_wind": max(winds),
        "avg_humidity": round(sum(hums) / len(hums), 1)
    }
    half = len(temps)//2 or 1
    trend = "stable"
    if sum(temps[:half]) / half < sum(temps[half:1]) / max(1, len(temps)-half):
        trend = "warming"
    elif sum(temps[:half]) / half > sum(temps[half:]) / max(1, len(temps)-half):
        trend = "cooling"
    avg["trend"] = trend
    return avg


# Demo usage example
if __name__ == "__main__":
    random.seed(42)  #  demo seed
    cities = [
        ("Lagos", "summer"),
        ("London", "fall"),
        ("New York", "winter"),
        ("Tokyo", "spring"),
    ]
    today = datetime.now().date()
    for city , season in cities:
        fc = generate_forecast(city, season, today, days=7)
        print(f"\n== 7-day forecast for {city} ({fc[0]['season']}) ===")
        for d in fc:
            warn = f" {d['warning']}" if d['warning'] else ""
            precip = f" {d['precip_mm']}mm" if d['precip_mm']>0 else ""
            print(f"{d['date']}: {d['emoji']} {d['condition']} | "
                  f"{d['temp_c']}°C "
                  f"(feels {d['feels_like_c']}°C) | "
                  f"Humidity {d['humidity']}% | "
                  f"Wind {d['wind_kmh']} km/h | "
                  f"Rain chance {d['rain_chance_pct']}%{precip}{warn}")
            summary = summarize_history(fc)
            print("\nSummary:", summary)


























