import json
from src.physics import calculate_cog_height, calculate_max_safe_angle

class HaulTruckSafetyChecker:
    def __init__(self, config_path):
        """Initialize with truck specs from a JSON file."""

        if isinstance(config_path, dict):
            self.truck_specs = config_path
        else:
            with open(config_path, 'r') as f:
                self.truck_specs = json.load(f)

    def check_safety(self, load_weight, angle_longitudinal, angle_lateral):
        """Check if the truck is safe given load and angles."""
        specs = self.truck_specs

        # Check if load exceeds maximum capacity
        if load_weight > specs["max_load"]:
            return {
                "status": "unsafe",
                "reason": "Load weight exceeds maximum capacity",
                "details": {"load_weight": load_weight, "max_load": specs["max_load"]}
            }

        # Calculate CoG height and maximum safe angles
        h = calculate_cog_height(load_weight, specs["max_load"], specs["h_empty"], specs["h_full"])
        theta_max_lat = calculate_max_safe_angle(specs["base_lateral"], h)
        theta_max_long = calculate_max_safe_angle(specs["base_longitudinal"], h)

        # Check lateral stability
        if abs(angle_lateral) > theta_max_lat:
            return {
                "status": "unsafe",
                "reason": "Lateral angle exceeds tipping limit",
                "details": {
                    "angle_lateral": angle_lateral,
                    "max_safe_lateral": theta_max_lat,
                    "cog_height": h
                }
            }

        # Check longitudinal stability
        if abs(angle_longitudinal) > theta_max_long:
            return {
                "status": "unsafe",
                "reason": "Longitudinal angle exceeds tipping limit",
                "details": {
                    "angle_longitudinal": angle_longitudinal,
                    "max_safe_longitudinal": theta_max_long,
                    "cog_height": h
                }
            }

        # If all checks pass, truck is safe
        return {
            "status": "safe",
            "details": {
                "load_weight": load_weight,
                "angle_longitudinal": angle_longitudinal,
                "angle_lateral": angle_lateral,
                "max_safe_lateral": theta_max_lat,
                "max_safe_longitudinal": theta_max_long,
                "cog_height": h
            }
        }