from solution import maxPoints
def test_one():
    points = [[1,1],[2,2],[3,3]]
    assert maxPoints(points)==3
def test_two():
    points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    assert maxPoints(points)==4