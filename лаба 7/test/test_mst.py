import unittest
import os
from src.mst_solver import calculate_min_cable_length

class TestMST(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_wells.csv"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def create_csv(self, data):
        with open(self.test_file, "w") as f:
            f.write(data)

    def test_standard_case(self):
        self.create_csv("K1,K2,2000\nK2,K3,1500\nK1,K3,3000")
        self.assertEqual(calculate_min_cable_length(self.test_file), 3500)

    def test_disconnected_graph(self):
        self.create_csv("K1,K2,1000\nK3,K4,500")
        self.assertEqual(calculate_min_cable_length(self.test_file), -1)

    def test_empty_file(self):
        self.create_csv("")
        self.assertEqual(calculate_min_cable_length(self.test_file), 0)

if __name__ == "__main__":
    unittest.main()