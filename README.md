# Haul Truck Safety Monitoring System

## Overview

The Haul Truck Safety Monitoring System is a Python-based tool designed to enhance safety in mining and heavy equipment operations. It assesses haul truck safety in real-time by analyzing load weight and tilt angles using physics-based calculations. This system helps operators identify tipping risks, making it an invaluable asset for predictive maintenance and safety management.

### Key Features

- **Physics-Based Safety Checks**: Calculates the center of gravity and tipping angles to determine safety risks.
- **Real-Time Monitoring**: Processes truck data snapshots for immediate safety feedback.
- **Configurable Truck Specs**: Easily adjust parameters to match different truck models.
- **Error Handling**: Provides robust validation and detailed error reporting.

---

## Installation

To get started, you’ll need **Python 3.6 or later**. The system relies solely on Python’s standard library, so no additional dependencies are required.

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/haul-truck-safety.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd haul-truck-safety
   ```

That’s it! You’re ready to use the system.

---

## Usage

The system operates through three core functions: `on_create`, `on_receive`, and `on_destroy`. These manage the safety monitor’s lifecycle from initialization to cleanup.

### Initialization

Start by initializing the safety monitor with truck specifications:

```python
truck_specs = {
    "max_load": 100.0,           # Maximum load capacity in tons
    "h_empty": 1.5,              # Height of center of gravity when empty (meters)
    "h_full": 2.5,               # Height of center of gravity when fully loaded (meters)
    "base_lateral": 3.0,         # Lateral base width (meters)
    "base_longitudinal": 5.0     # Longitudinal base length (meters)
}

result = on_create(truck_specs)
print(result)  # Output: {"status": "initialized"}
```

### Processing Snapshots

To evaluate safety, provide a snapshot of the truck’s current state:

```python
snapshot = {
    "load_weight": 50.0,         # Current load weight in tons
    "angle_longitudinal": 10.0,  # Longitudinal tilt angle in degrees
    "angle_lateral": 20.0        # Lateral tilt angle in degrees
}

result = on_receive(snapshot)
print(result)  # Example output: {"status": "safe", "details": {...}}
```

The response will indicate whether the truck is safe or at risk, along with additional details.

### Cleanup

When done, clean up resources:

```python
result = on_destroy()
print(result)  # Output: {"status": "destroyed"}
```

---

## Configuration

Accurate truck specifications are essential for reliable safety checks. Here’s what each parameter means:

- **`max_load`**: Maximum safe load weight (tons).
- **`h_empty`**: Center of gravity height when the truck is empty (meters).
- **`h_full`**: Center of gravity height when fully loaded (meters).
- **`base_lateral`**: Width between the truck’s wheels for lateral stability (meters).
- **`base_longitudinal`**: Length between axles for longitudinal stability (meters).

Adjust these values to match your specific haul truck model.

---

## Contributing

We’d love your help to make this system even better! If you spot a bug or have an idea for improvement, please:

1. Open an issue on the [GitHub repository](https://github.com/yourusername/haul-truck-safety).
2. Share your feedback or suggestions.

Your contributions are greatly appreciated!
