from solution import canCompleteCircuit
def test_one():
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    assert canCompleteCircuit(gas, cost)==3
def test_two():
    gas = [2,3,4]
    cost = [3,4,3]
    assert canCompleteCircuit(gas, cost)==-1