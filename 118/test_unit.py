from solution import generate
def test_one():
    numRows = 5
    assert generate(numRows)==[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

def test_two():
    numRows = 1
    assert generate(numRows)==[[1]]