import unittest

from patient_flow_forecaster.models import Record
from patient_flow_forecaster.scoring import score_record


class DepthCheck62(unittest.TestCase):
    def test_062_operator_handoff(self):
        record = Record(id="encounter-062", exposure=94226, signal=0.531, urgency=4)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
