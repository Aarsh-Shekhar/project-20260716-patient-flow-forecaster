import unittest

from patient_flow_forecaster.models import Record
from patient_flow_forecaster.scoring import score_record


class DepthCheck47(unittest.TestCase):
    def test_047_control_mapping(self):
        record = Record(id="encounter-047", exposure=83628, signal=0.619, urgency=8)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
