import pytest

from olxbrasil.constants import STATES, STATES_DDD


@pytest.mark.parametrize("key,value", STATES.items())
def test_state_constant(states, key, value):
    assert key in states, f"{key} is not in states"
    assert value.upper() in states, f"{value} is not in states"


@pytest.mark.parametrize("key,value", STATES_DDD.items())
def test_ddd_constants(ddd_constants, states_names_constants, key, value):
    assert key in ddd_constants, f"{key} is not on DDD list"
    assert (
        value in states_names_constants
    ), f"{value} is not in State Name list"
