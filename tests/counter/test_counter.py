import pytest
from src.pre_built.counter import count_ocurrences


def test_counter():
    words = count_ocurrences('data/jobs.csv', 'city')
    assert words == 539


def test_counter2():
    words = count_ocurrences('data/jobs.csv', 'city')
    assert words != 0


def test_counter3():
    with pytest.raises(
        AttributeError, match="'int' object has no attribute 'lower'"
    ):
        count_ocurrences('data/jobs.csv', 5)
