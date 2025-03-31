import json
from src.safety_checker import HaulTruckSafetyChecker

# Global variable to hold the safety checker instance
safety_checker = None

# Top-level functions as required
def on_create(data: dict) -> dict:
    """
    Initialize the safety monitor with truck specifications.
    
    Args:
        data (dict): Truck specifications (e.g., max_load, h_empty, h_full, base_lateral, base_longitudinal)
    
    Returns:
        dict: Status of initialization (e.g., {"status": "initialized"} or {"error": "message"})
    """
    global safety_checker
    try:
        safety_checker = HaulTruckSafetyChecker()
        return {"status": "initialized"}
    except Exception as e:
        return {"error": str(e)}

def on_receive(data: dict) -> dict:
    """
    Process a snapshot of truck data and perform a safety check.
    
    Args:
        data (dict): Snapshot data (e.g., load_weight, angle_longitudinal, angle_lateral)
    
    Returns:
        dict: Safety check result (e.g., {"status": "safe", "details": {...}} or {"error": "message"})
    """
    print("!on_receive")
    print(data)
    global safety_checker
    if safety_checker is None:
        print("!on_receive: safety_checker is None")
        return {"error": "Monitor not initialized"}
    try:

        result = safety_checker.check_safety(
            data["load_weight"],
            data["angle_longitudinal"],
            data["angle_lateral"],
            {"load_weight": data["spec_load_weight"], 
             "angle_longitudinal": data["spec_angle_longitudinal"], 
             "angle_lateral": data["spec_angle_lateral"],
            "max_load": data["spec_max_load"],
            "h_empty": data["spec_h_empty"],
            "h_full": data["spec_h_full"],
            "base_lateral": data["spec_base_lateral"],
            "base_longitudinal": data["spec_base_longitudinal"]}
        )
        print(result)
        return {"result": result}
    except Exception as e:
        print(f"Error: {str(e)}")
        return {"error": str(e)}

def on_destroy() -> dict:
    """
    Clean up the safety monitor.
    
    Returns:
        dict: Status of destruction (e.g., {"status": "destroyed"})
    """
    global safety_checker
    safety_checker = None
    return {"status": "destroyed"}

# Example usage
if __name__ == "__main__":
    # Example truck specifications
    truck_specs = {
        "max_load": 100.0,
        "h_empty": 1.5,
        "h_full": 2.5,
        "base_lateral": 3.0,
        "base_longitudinal": 5.0
    }
    
    # Initialize the monitor
    print("on_create:", on_create(truck_specs))
    
    # Example snapshot
    snapshot = {
        "load_weight": 50.0,
        "angle_longitudinal": 10.0,
        "angle_lateral": 20.0
    }
    
    # Process the snapshot
    print("on_receive:", on_receive(snapshot))
    
    # Destroy the monitor
    print("on_destroy:", on_destroy())