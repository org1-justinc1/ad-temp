import backend.add

def test_noop():
    assert True
    # assert 11==0

def test_add():
    assert backend.add.add(10, 20) == 30
