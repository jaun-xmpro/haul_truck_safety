import json
from src.safety_checker import HaulTruckSafetyChecker

def main():
    # Load configuration
    config_path = "config/truck_specs.json"
    checker = HaulTruckSafetyChecker(config_path)

    # Example input (could come from a file, API, or sensor)
    input_data = {
        "load_weight": 50.0,
        "angle_longitudinal": 10.0,
        "angle_lateral": 20.0
    }

    try:
        result = checker.check_safety(**input_data)
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()