import math

def calculate_cog_height(load_weight, max_load, h_empty, h_full):
    """Calculate the center of gravity height based on load."""
    load_ratio = load_weight / max_load
    return h_empty + load_ratio * (h_full - h_empty)

def calculate_max_safe_angle(base, cog_height):
    """Calculate the maximum safe tilt angle before tipping."""
    return math.degrees(math.atan((base / 2) / cog_height))