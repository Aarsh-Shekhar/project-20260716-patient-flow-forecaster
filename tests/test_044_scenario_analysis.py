import unittest

from patient_flow_forecaster.models import Record
from patient_flow_forecaster.scoring import score_record


class DepthCheck44(unittest.TestCase):
    def test_044_scenario_analysis(self):
        record = Record(id="encounter-044", exposure=43548, signal=0.541, urgency=6)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
