def test_method():
    import os
    print(os.getcwd());

from src.pypi_packaging_tutorial.core import example_function, add_two, ExampleClass

def test_example_function():
    assert my_function(1, 2) == 3

def test_add_two():
    assert add_two(5)==7;



def test_example_class():
    instance = ExampleClass()
    assert instance.example_class_method() == "expected result"
