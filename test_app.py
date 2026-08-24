from app import add,subtract,multiply,divide
def test_add():
    assert add(20, 30) == 50
def test_subtract():
    assert subtract(20, 30) == -10

def test_multiply():
    assert multiply(20, 30) == 600

def test_divide():
    assert divide(20, 30) == 2/3