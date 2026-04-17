import unittest, tempfile, csv
from pathlib import Path
from parse_launch_weather import summarize
class SensorChecks(unittest.TestCase):
    def test_corruption_and_rolling_coverage(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory)/'summary.csv'
            accepted, rejected = summarize('sample_canaveral_met.csv', destination)
            self.assertEqual((accepted,rejected),(96,4))
            with destination.open() as stream:
                rows = list(csv.DictReader(stream))
            self.assertLessEqual(max(int(row['window_observations']) for row in rows),15)
