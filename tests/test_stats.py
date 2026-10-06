"""describe-stats-cli 单元测试。运行：python3 -m unittest discover -s tests"""
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from stats import describe  # noqa: E402


class TestStats(unittest.TestCase):
    def test_mean(self):
        d = describe([1, 2, 3, 4, 5])
        self.assertEqual(d["mean"], 3.0)

    def test_median(self):
        self.assertEqual(describe([1, 2, 30])["median"], 2)

    def test_mode(self):
        self.assertEqual(describe([1, 1, 2, 3])["mode"], 1)

    def test_variance(self):
        d = describe([2, 4])
        self.assertEqual(d["variance"], 1.0)

    def test_quantile(self):
        d = describe([1, 2, 3, 4])
        self.assertIn("p25", d)
        self.assertLessEqual(d["p25"], d["p75"])

    def test_skewness_symmetric(self):
        d = describe([1, 2, 3, 4, 5])
        self.assertAlmostEqual(d["skewness"], 0.0, places=1)

    def test_empty(self):
        self.assertEqual(describe([]), {"count": 0})


if __name__ == "__main__":
    unittest.main()
