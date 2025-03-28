import unittest
from src.safety_checker import HaulTruckSafetyChecker

class TestSafetyChecker(unittest.TestCase):
    def setUp(self):
        self.checker = HaulTruckSafetyChecker("config/truck_specs.json")

    def test_safe_condition(self):
        result = self.checker.check_safety(50.0, 10.0, 20.0)
        self.assertEqual(result["status"], "safe")

    def test_unsafe_load(self):
        result = self.checker.check_safety(150.0, 0.0, 0.0)
        self.assertEqual(result["status"], "unsafe")
        self.assertIn("Load weight exceeds maximum capacity", result["reason"])

    def test_unsafe_lateral_angle(self):
        result = self.checker.check_safety(50.0, 0.0, 40.0)
        self.assertEqual(result["status"], "unsafe")
        self.assertIn("Lateral angle exceeds tipping limit", result["reason"])

if __name__ == "__main__":
    unittest.main()