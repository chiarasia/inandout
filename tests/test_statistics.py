from src.statistics import total_sessions

def test_statistics():

    assert total_sessions() >= 0
