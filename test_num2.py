import pytest
import logging


def sum(num1, num2):
    return num1 + num2


test1 = (1, 2, 3)
test2 = (2, 3, 5)
test3 = (3, 3, 6)
list2 = [1, 2, 3]
login = {'admin', '12345', 'll', '124'}


@pytest.mark.parametrize(
    "a,b,wish",
    [
        test1,
        test2,
        test3,
    ]
)
def testsum(a, b, wish):
    assert sum(a, b) == wish
    for name in list2:
        print(str(name))
        # logging.INFO(str(name))


def test33():
    pass
