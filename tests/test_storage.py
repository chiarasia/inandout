from src.storage import load_sessions

def test_storage():

    assert isinstance(load_sessions(), list)
