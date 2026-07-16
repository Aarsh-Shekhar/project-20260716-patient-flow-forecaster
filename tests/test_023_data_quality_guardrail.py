import unittest

from patient_flow_forecaster.models import Record
from patient_flow_forecaster.scoring import score_record


class DepthCheck23(unittest.TestCase):
    def test_023_data_quality_guardrail(self):
        record = Record(id="encounter-023", exposure=85751, signal=0.451, urgency=5)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
