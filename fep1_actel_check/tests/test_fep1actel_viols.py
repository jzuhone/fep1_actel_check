from ..fep1_actel_check import model_path, FEP1ActelCheck
from acis_thermal_check.regression_testing import \
    RegressionTester, all_loads
import pytest
import os


def test_JUL3019A_viols(answer_store, test_root):
    answer_data = os.path.join(os.path.dirname(__file__), "answers",
                               "JUL2919A_viol.json")
    fa_rt = RegressionTester(FEP1ActelCheck, model_path,
                             "fep1_actel_test_spec.json",
                             test_root=test_root, sub_dir='viols')
    fa_rt.check_violation_reporting("JUL2919A", answer_data,
                                    answer_store=answer_store)