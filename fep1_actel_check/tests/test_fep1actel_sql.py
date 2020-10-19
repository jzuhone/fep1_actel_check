from ..fep1_actel_check import model_path, FEP1ActelCheck
from acis_thermal_check.regression_testing import \
    RegressionTester, all_loads
import pytest

@pytest.fixture(autouse=True, scope='module')
def fa_rt(test_root):
    # SQL state builder tests
    rt = RegressionTester(FEP1ActelCheck, model_path,
                          "fep1_actel_test_spec.json",
                          test_root=test_root, sub_dir='sql')
    rt.run_models(state_builder='sql')
    return rt

# Prediction tests


@pytest.mark.parametrize('load', all_loads)
def test_prediction(fa_rt, answer_store, load):
    if not answer_store:
        fa_rt.run_test("prediction", load)
    else:
        pass

# Validation tests


@pytest.mark.parametrize('load', all_loads)
def test_validation(fa_rt, answer_store, load):
    if not answer_store:
        fa_rt.run_test("validation", load)
    else:
        pass
