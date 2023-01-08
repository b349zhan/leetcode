from solution import maxIceCream

def test_one():
    costs = [1,3,2,4,1]
    coins = 7
    assert(maxIceCream(costs, coins)==4)

def test_two():
    costs = [10, 6, 8, 7, 7, 8]
    coins = 5
    assert(maxIceCream(costs, coins)==0)

def test_three():
    costs=[1, 6, 3, 1, 2, 5]
    coins = 20
    assert(maxIceCream(costs, coins)==6)