from ..fep1_actel_check import model_path, FEP1ActelCheck
from acis_thermal_check.regression_testing import \
    RegressionTester, all_loads
import pytest

fep1actel_rt = RegressionTester(FEP1ActelCheck, model_path, "fep1_actel_test_spec.json")

# ACIS state builder tests

fep1actel_rt.run_models(state_builder='acis')

# Prediction tests


@pytest.mark.parametrize('load', all_loads)
def test_prediction(answer_store, load):
    fep1actel_rt.run_test("prediction", load, answer_store=answer_store)

# Validation tests


@pytest.mark.parametrize('load', all_loads)
def test_validation(answer_store, load):
    fep1actel_rt.run_test("validation", load, answer_store=answer_store)
