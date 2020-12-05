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


if __name__ == '__main__':
    lis = [1, 2, 3, 4, 4]
    # 返回的是索引 index(value,start,stop)
    print(lis.index(2, 0, 3))
    # count(value) 返回值的个数 时间复杂度O(n) 同index
    print(lis.count(4))
    # append(object) 返回None 时间复杂度O(1)
    lis.append(2)
    print(lis)
    # insert(index,object) 时间复杂度O(n)
    lis.insert(3, 999)
    print(lis)
    #批量扩展列表的value
    lis.extend([4, 4, 4, 4, 4])
    print(lis)

    lis.reverse()
