from src.calculator import add, divide

def test_add():
    assert add(2, 3) == 5

def test_divide():
    # INTENTIONAL ERROR: This will crash with a ZeroDivisionError to test the AI-Ops Pipeline
    assert divide(10, 0) == 0
