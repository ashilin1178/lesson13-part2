import pytest
from utils import double, ticket_price


# параметризация теста
@pytest.mark.parametrize(
    "test_input, expected",
    [(0, 0), (1, 2), (10.0, 20.0), (-3, -6), (123456789, 246913578)]
)
def test_double(test_input, expected):
    assert double(test_input) == expected


@pytest.mark.parametrize(
    'test_input, expected',
    [(0, "Бесплатно"), (60, "Бесплатно"), (1, "Бесплатно"), (7, "100 рублей"), (18, "200 рублей"), (25, "300 рублей"),
     (0.5, "Бесплатно"), (-1, "Ошибка")]
)
def test_ticket_price(test_input, expected):
    assert ticket_price(test_input) == expected
