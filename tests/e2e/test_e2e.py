# tests/e2e/test_e2e.py

import pytest  # Import the pytest framework for writing and running tests

# The following decorators and functions define E2E tests for the FastAPI calculator application.

# @pytest.mark.e2e is a custom marker used in pytest to label a test as an end-to-end (E2E) test.
# It tags the test so you can:
    # Identify it as an E2E test (i.e. tests that simulate full app usage from the user’s perspective).
    # Run only E2E tests when you want:
        # pytest -m e2e in terminal
    # Exclude E2E tests from a quick test run:
        # pytest -m "not e2e" in terminal
@pytest.mark.e2e
def test_hello_world(page, fastapi_server):
    """
    Test that the homepage displays "Hello World".

    This test verifies that when a user navigates to the homepage of the application,
    the main header (`<h1>`) correctly displays the text "Hello World". This ensures
    that the server is running and serving the correct template.
    """
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Use an assertion to check that the text within the first <h1> tag is exactly "Hello World".
    # If the text does not match, the test will fail.
    assert page.inner_text('h1') == 'Hello World'

@pytest.mark.e2e
def test_calculator_add(page, fastapi_server):
    """
    Test the addition functionality of the calculator.

    This test simulates a user performing an addition operation using the calculator
    on the frontend. It fills in two numbers, clicks the "Add" button, and verifies
    that the result displayed is correct.
    """
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Fill in the first number input field (with id 'a') with the value '17'.
    page.fill('#a', '7')
    
    # Fill in the second number input field (with id 'b') with the value '23'.
    page.fill('#b', '3')
    
    # Click the button that has the exact text "Add". This triggers the addition operation.
    page.click('button:text("Add")')
    
    # Use an assertion to check that the text within the result div (with id 'result') is exactly "Result: 10".
    # This verifies that the addition operation was performed correctly and the result is displayed as expected.
    assert page.inner_text('#result') == 'Result: 10'

@pytest.mark.e2e
def test_calculator_divide_by_zero(page, fastapi_server):
    """
    Test the divide by zero functionality of the calculator.

    This test simulates a user attempting to divide a number by zero using the calculator.
    It fills in the numbers, clicks the "Divide" button, and verifies that the appropriate
    error message is displayed. This ensures that the application correctly handles invalid
    operations and provides meaningful feedback to the user.
    """
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Fill in the first number input field (with id 'a') with the value '60'.
    page.fill('#a', '60')
    
    # Fill in the second number input field (with id 'b') with the value '0', attempting to divide by zero.
    page.fill('#b', '0')
    
    # Click the button that has the exact text "Divide". This triggers the division operation.
    page.click('button:text("Divide")')
    
    # Use an assertion to check that the text within the result div (with id 'result') is exactly
    # "Error: Cannot divide by zero!". This verifies that the application handles division by zero
    # gracefully and displays the correct error message to the user.
    assert page.inner_text('#result') == 'Error: Cannot divide by zero!'

def test_calculator_subtraction(page, fastapi_server):
    """
    Test the subtraction functionality of the calculator.
    Simulates a user performing a subtraction operation using the calculator UI
    """

    # go to home page
    page.goto('http://localhost:8000')

    # fill in first and second numbers (67 and 34 respectively)
    page.fill('#a', '60')
    page.fill('#b', '34')

    page.click('button:text("Subtract")')

    assert page.inner_text('#result') == 'Result: 26'


def test_calculator_multiplication(page, fastapi_server):
    """
    Test the multiplication functionality of the calculator.
    Simulates a user performing a multiplication operation using the calculator UI
    """

    # go to home page
    page.goto('http://localhost:8000')

    # fill in first and second numbers (67 and 34 respectively)
    page.fill('#a', '12')
    page.fill('#b', '12')

    page.click('button:text("Multiply")')

    assert page.inner_text('#result') == 'Result: 144'

def test_calculator_division(page, fastapi_server):
    """
    Test the division functionality of the calculator.
    Simulates a user performing a division operation using the calculator UI
    """

    # go to home page
    page.goto('http://localhost:8000')

    # fill in first and second numbers (67 and 34 respectively)
    page.fill('#a', '60')
    page.fill('#b', '12')

    page.click('button:text("Divide")')

    assert page.inner_text('#result') == 'Result: 5'
