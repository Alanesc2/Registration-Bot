import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import getpass
import time
from datetime import datetime, timedelta

semester = None

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-gpu')
    options.page_load_strategy = 'normal'
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def get_user_input():
    username = input("Username: ")
    password = getpass.getpass("Password: ")  
    user_time = input("Registration Time (MM/DD/YYYY HH:MM AM/PM): ")

    try:
        reg_time = datetime.strptime(user_time, "%m/%d/%Y %I:%M %p")
    except ValueError:
        print("Invalid date format. Please use MM/DD/YYYY HH:MM AM/PM.")
        return None

    if 2 <= reg_time.month <= 7:
        semester = input(f"Are you registering for Fall {reg_time.year}? Say yes if so, otherwise (YYYY Semester): ")
        if (semester == "yes"):
            semester = "{reg_time.year} Fall"
    
    else:
        semester = input(f"Are you registering for spring {reg_time.year}? Say yes if so, otherwise (Semester/YYYY): ")
        if (semester == "yes"):
            semester = "{reg_time.year} Spring"

    return username, password, reg_time, semester

def wait_until_time(target_time, offset_minutes=5):
    login_time = target_time - timedelta(minutes=offset_minutes)
    while datetime.now() < login_time:
        time.sleep(30)

def login(driver, username, password):
    driver.get("https://my.asu.edu") 
    wait = WebDriverWait(driver, 20)

    username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
    time.sleep(2)
    username_field.clear()
    username_field.send_keys(username)

    password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
    time.sleep(2)
    password_field.clear()
    password_field.send_keys(password)

    time.sleep(2)
    
    password_field.send_keys(Keys.RETURN)

def bypass_2fa(driver):
    try:
        wait = WebDriverWait(driver, 15)
        yes_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Yes, this is my device')]")))
        time.sleep(1)
        yes_button.click()
        print("2FA bypass successful.")
    except:
        print("2FA bypass not required or failed.")

def register_classes(driver, semester, reg_time):
    try:
        wait = WebDriverWait(driver, 20)

        try:
            reg_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Registration")))
            if reg_button:
                print(f"Found registration button")
        except:
            print(f"Error: {e}")
        
        if not reg_button:
            print("Page source:")
            print(driver.page_source)
            raise Exception("Could not find registration button")
        
        time.sleep(2)
        
        try:
            reg_button.click()
        except:
            driver.execute_script("arguments[0].click();", reg_button)
        
        time.sleep(3)
        
        try:
            cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Add/Shopping Cart')]")))
            cart_button.click()
            time.sleep(2)
        except:
            print(f"Could not click {cart} button")

        try:
            reg_text = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ps_box-value")))

            reg_semester = reg_text.text.strip()
            print(reg_semester) 

        except Exception as e:
            print(f"Error finding semester element: {e}")



        if reg_semester != semester:
            change_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='DERIVED_SSR_FL_SSR_CHANGE_BTN' and contains(@class, 'ps-button')]")))
            WebDriverWait(driver, 2)
            change_button.click()

            choose_sem = wait.until(EC.element_to_be_clickable((By.XPATH, f"//button[contains(text(), '{semester}')]"))) 
            choose_sem.click()

        actual_cart = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Shopping Cart')]")))
        actual_cart.click()

        try:
            actual_cart = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//a[contains(text(), 'Shopping Cart')]")))
            actual_cart.click()
            time.sleep(2)
        except Exception as e:
            print(f"Error accessing shopping cart: {e}")

        while datetimetime.now < reg_time:
            time.sleep(1)

        enroll_button = wait.until(EC.element_to_be_clickable((By.ID, "DERIVED_REGFRM1_SSR_PB_SUBMIT")))
        print("Clicking Enroll button...")
        enroll_button.click()
        time.sleep(3)


    except Exception as e:
        print(f"Error in register_classes: {e}")
        import traceback
        traceback.print_exc()

def main():
    user_data = get_user_input()
    if user_data:
        username, password, reg_time, semester = user_data
        print(f"Got it! Regbot will now register your classes at {reg_time.strftime('%m/%d/%Y %I:%M %p')}")
    driver = None
    try:
        driver = setup_driver()
        wait_until_time(reg_time)
        login(driver, username, password)
        bypass_2fa(driver)
        register_classes(driver, semester, reg_time)
        time.sleep(10)
    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    main()