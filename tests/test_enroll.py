import pytest
from datetime import datetime
from unittest.mock import patch, MagicMock
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Import the functions we want to test
from enroll import get_user_input, wait_until_time, setup_driver

def test_get_user_input_valid():
    """Test get_user_input with valid input"""
    test_inputs = [
        "testuser",
        "testpass",
        "12/25/2024 10:00 AM",
        "yes"
    ]
    
    with patch('builtins.input', side_effect=test_inputs):
        with patch('getpass.getpass', return_value=test_inputs[1]):
            result = get_user_input()
            
    assert result is not None
    username, password, reg_time, semester = result
    assert username == "testuser"
    assert password == "testpass"
    assert isinstance(reg_time, datetime)
    assert semester == "2024 Fall"

def test_get_user_input_invalid_date():
    """Test get_user_input with invalid date format"""
    test_inputs = [
        "testuser",
        "testpass",
        "invalid_date",
        "yes"
    ]
    
    with patch('builtins.input', side_effect=test_inputs):
        with patch('getpass.getpass', return_value=test_inputs[1]):
            result = get_user_input()
            
    assert result is None

@pytest.mark.selenium
def test_setup_driver():
    """Test driver setup"""
    driver = setup_driver()
    assert driver is not None
    driver.quit()

def test_wait_until_time():
    """Test wait_until_time function"""
    target_time = datetime.now()
    with patch('time.sleep') as mock_sleep:
        wait_until_time(target_time, offset_minutes=1)
        assert mock_sleep.called

@pytest.fixture
def mock_driver():
    """Fixture to create a mock Selenium driver"""
    driver = MagicMock()
    return driver

def test_login(mock_driver):
    """Test login function"""
    from enroll import login
    
    # Mock the WebDriverWait and its until method
    mock_wait = MagicMock()
    mock_element = MagicMock()
    mock_wait.until.return_value = mock_element
    
    with patch('selenium.webdriver.support.ui.WebDriverWait', return_value=mock_wait):
        with patch('time.sleep'):
            login(mock_driver, "testuser", "testpass")
            
    assert mock_driver.get.called
    assert mock_element.send_keys.called

def test_bypass_2fa(mock_driver):
    """Test 2FA bypass function"""
    from enroll import bypass_2fa
    
    # Mock the WebDriverWait and its until method
    mock_wait = MagicMock()
    mock_button = MagicMock()
    mock_wait.until.return_value = mock_button
    
    with patch('selenium.webdriver.support.ui.WebDriverWait', return_value=mock_wait):
        with patch('time.sleep'):
            bypass_2fa(mock_driver)
            
    assert mock_button.click.called 