import pytest
from function import amount_of_vehicle

@pytest.mark.code
def test_input_sdf():
    input = 'sdf'
    expected_result = "Input must be an integer"
    actual_result = amount_of_vehicle(input)
    assert expected_result == actual_result

@pytest.mark.code
def test_input_1():
    input = -1
    expected_result = "Input must be a non-negative integer"
    actual_result = amount_of_vehicle(input)
    assert expected_result == actual_result

@pytest.mark.code
def test_input_0():
    input = 0
    expected_result = "No vehicle needed"
    actual_result = amount_of_vehicle(input)
    assert expected_result == actual_result

 # Test cases for van only 
@pytest.mark.code
def test_input_22():
    input = 22
    expected_result = "2 van(s) needed"
    actual_result = amount_of_vehicle(input)
    assert expected_result == actual_result
    
@pytest.mark.code
def test_input_33():
    input = 33
    expected_result = "3 van(s) needed"
    actual_result = amount_of_vehicle(input)
    assert expected_result == actual_result
    


# Test cases for van and car
@pytest.mark.code
def test_input_12():
    input = 12
    expected_result = "1 van(s) and 1 car(s) needed"
    actual_result = amount_of_vehicle(input)
    assert expected_result == actual_result
    
@pytest.mark.code
def test_input_17():
    input = 17
    expected_result = "1 van(s) and 2 car(s) needed"
    actual_result = amount_of_vehicle(input)
    assert expected_result == actual_result
    
@pytest.mark.code
def test_input_20():
    input = 20
    expected_result = "1 van(s) and 3 car(s) needed"
    actual_result = amount_of_vehicle(input)
    assert expected_result == actual_result
    
@pytest.mark.code
def test_input_23():
    input = 23
    expected_result = "2 van(s) and 1 car(s) needed"
    actual_result = amount_of_vehicle(input)
    assert expected_result == actual_result

@pytest.mark.code
def test_input_29():
    input = 29
    expected_result = "2 van(s) and 2 car(s) needed"
    actual_result = amount_of_vehicle(input)
    assert expected_result == actual_result

@pytest.mark.code
def test_input_32():
    input = 32
    expected_result = "2 van(s) and 3 car(s) needed"
    actual_result = amount_of_vehicle(input)
    assert expected_result == actual_result
    
@pytest.mark.code
def test_input_34():
    input = 34
    expected_result = "3 van(s) and 1 car(s) needed"
    actual_result = amount_of_vehicle(input)
    assert expected_result == actual_result
    
@pytest.mark.code
def test_input_45():
    input = 45
    expected_result = "4 van(s) and 1 car(s) needed"
    actual_result = amount_of_vehicle(input)
    assert expected_result == actual_result
    
@pytest.mark.code
def test_input_51():
    input = 51
    expected_result = "4 van(s) and 2 car(s) needed"
    actual_result = amount_of_vehicle(input)
    assert expected_result == actual_result

@pytest.mark.code
def test_input_54():
    input = 54
    expected_result = "4 van(s) and 3 car(s) needed"
    actual_result = amount_of_vehicle(input)
    assert expected_result == actual_result

@pytest.mark.code
def test_input_56():
    input = 56
    expected_result = "5 van(s) and 1 car(s) needed"
    actual_result = amount_of_vehicle(input)
    assert expected_result == actual_result
   
@pytest.mark.code
def test_input_62():
    input = 62
    expected_result = "5 van(s) and 2 car(s) needed"
    actual_result = amount_of_vehicle(input)
    assert expected_result == actual_result
 
@pytest.mark.code
def test_input_65():
    input = 65
    expected_result = "5 van(s) and 3 car(s) needed"
    actual_result = amount_of_vehicle(input)
    assert expected_result == actual_result
 
 
# Test cases for car only   
@pytest.mark.code
def test_input_1():
    input = 1
    expected_result = "1 car(s) needed"
    actual_result = amount_of_vehicle(input)
    assert expected_result == actual_result
    
@pytest.mark.code
def test_input_2():
    input = 3
    expected_result = "1 car(s) needed"
    actual_result = amount_of_vehicle(input)
    assert expected_result == actual_result

@pytest.mark.code
def test_input_4():
    input = 4
    expected_result = "1 car(s) needed"
    actual_result = amount_of_vehicle(input)
    assert expected_result == actual_result

@pytest.mark.code
def test_input_5():
    input = 5
    expected_result = "2 car(s) needed"
    actual_result = amount_of_vehicle(input)
    assert expected_result == actual_result

@pytest.mark.code
def test_input_6():
    input = 6
    expected_result = "2 car(s) needed"
    actual_result = amount_of_vehicle(input)
    assert expected_result == actual_result

@pytest.mark.code
def test_input_7():
    input = 7
    expected_result = "2 car(s) needed"
    actual_result = amount_of_vehicle(input)
    assert expected_result == actual_result

@pytest.mark.code
def test_input_8():
    input = 8
    expected_result = "2 car(s) needed"
    actual_result = amount_of_vehicle(input)
    assert expected_result == actual_result
    
@pytest.mark.code
def test_input_9():
    input = 9
    expected_result = "3 car(s) needed"
    actual_result = amount_of_vehicle(input)
    assert expected_result == actual_result
    
@pytest.mark.code
def test_input_10():
    input = 10
    expected_result = "3 car(s) needed"
    actual_result = amount_of_vehicle(input)
    assert expected_result == actual_result