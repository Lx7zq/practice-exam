from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_path = "D:\\webdriver\\chromedriver.exe"
service = Service(chrome_path)
driver = webdriver.Chrome(service=service)

def take_screenshot(driver, filename):
    driver.save_screenshot(filename)

def test_case1():
    driver = webdriver.Chrome(executable_path="D:\\webdriver\\chromedriver.exe")
    driver.get("http://localhost/Customer/form.html")
    
    firstNameInput = driver.find_element_by_id("first-name")
    lastNameInput = driver.find_element_by_id("last-name")
    ageInput = driver.find_element_by_id("age")
    submitButton = driver.find_element_by_id("sub")
    
    firstNameInput.send_keys("johnjohn")
    lastNameInput.send_keys("canonc")
    ageInput.send_keys("2")

    # Submit the form
    submitButton.click()
    
    take_screenshot(driver, "test_case1.png")
    
    result = driver.find_element_by_id("firstname").text
    assert result == "First Name: johnjohn"
    
    driver.close()

def test_case2():
    driver = webdriver.Chrome(executable_path="D:\\webdriver\\chromedriver.exe")
    driver.get("http://localhost/Customer/form.html")
    
    firstNameInput = driver.find_element_by_id("first-name")
    lastNameInput = driver.find_element_by_id("last-name")
    ageInput = driver.find_element_by_id("age")
    submitButton = driver.find_element_by_id("sub")
    
    firstNameInput.send_keys("Johnj")
    lastNameInput.send_keys("canoncanoncano")
    ageInput.send_keys("149")

    # Submit the form
    submitButton.click()
    
    take_screenshot(driver, "test_case2.png")
    
    result = driver.find_element_by_id("firstname").text
    assert result == "First Name: Johnj"
    
    driver.close()

def test_case3():
    driver = webdriver.Chrome(executable_path="D:\\webdriver\\chromedriver.exe")
    driver.get("http://localhost/Customer/form.html")
    
    firstNameInput = driver.find_element_by_id("first-name")
    lastNameInput = driver.find_element_by_id("last-name")
    ageInput = driver.find_element_by_id("age")
    submitButton = driver.find_element_by_id("sub")
    
    firstNameInput.send_keys("johnjo")
    lastNameInput.send_keys("canoncanoncanon")
    ageInput.send_keys("150")

    # Submit the form
    submitButton.click()
    
    take_screenshot(driver, "test_case3.png")
    
    result = driver.find_element_by_id("firstname").text
    assert result == "First Name: johnjo"
    
    driver.close()

def test_case4():
    driver = webdriver.Chrome(executable_path="D:\\webdriver\\chromedriver.exe")
    driver.get("http://localhost/Customer/form.html")
    
    firstNameInput = driver.find_element_by_id("first-name")
    lastNameInput = driver.find_element_by_id("last-name")
    ageInput = driver.find_element_by_id("age")
    submitButton = driver.find_element_by_id("sub")
    
    firstNameInput.send_keys("johnjohnjohnjo")
    lastNameInput.send_keys("canoncan")
    ageInput.send_keys("75")

    # Submit the form
    submitButton.click()
    
    take_screenshot(driver, "test_case4.png")
    
    result = driver.find_element_by_id("firstname").text
    assert result == "First Name: johnjohnjohnjo"
    
    driver.close()

def test_case5():
    driver = webdriver.Chrome(executable_path="D:\\webdriver\\chromedriver.exe")
    driver.get("http://localhost/Customer/form.html")
    
    firstNameInput = driver.find_element_by_id("first-name")
    lastNameInput = driver.find_element_by_id("last-name")
    ageInput = driver.find_element_by_id("age")
    submitButton = driver.find_element_by_id("sub")
    
    firstNameInput.send_keys("johnjohnjohnjoh")
    lastNameInput.send_keys("canoncan")
    ageInput.send_keys("75")

    # Submit the form
    submitButton.click()
    
    take_screenshot(driver, "test_case5.png")
    
    result = driver.find_element_by_id("firstname").text
    assert result == "First Name: johnjohnjohnjoh"
    
    driver.close()

def test_case6():
    driver = webdriver.Chrome(executable_path="D:\\webdriver\\chromedriver.exe")
    driver.get("http://localhost/Customer/form.html")
    
    firstNameInput = driver.find_element_by_id("first-name")
    lastNameInput = driver.find_element_by_id("last-name")
    ageInput = driver.find_element_by_id("age")
    submitButton = driver.find_element_by_id("sub")
    
    firstNameInput.send_keys("John")
    lastNameInput.send_keys("cannoncan")
    ageInput.send_keys("75")

    # Submit the form
    submitButton.click()
    
    take_screenshot(driver, "test_case6.png")
    
    result = driver.find_element_by_id("formname").text
    assert result == "Customer Detail Form"
    
    driver.close()

def test_case8():
    driver = webdriver.Chrome(executable_path="D:\\webdriver\\chromedriver.exe")
    driver.get("http://localhost/Customer/form.html")
    
    firstNameInput = driver.find_element_by_id("first-name")
    lastNameInput = driver.find_element_by_id("last-name")
    ageInput = driver.find_element_by_id("age")
    submitButton = driver.find_element_by_id("sub")
    
    firstNameInput.send_keys("johnjohn")
    lastNameInput.send_keys("cano")
    ageInput.send_keys("75")

    # Submit the form
    submitButton.click()
    
    take_screenshot(driver, "test_case8.png")
    
    result = driver.find_element_by_id("formname").text
    assert result == "Customer Detail Form"
    
    driver.close()


def test_case10():
    driver = webdriver.Chrome(executable_path="D:\\webdriver\\chromedriver.exe")
    driver.get("http://localhost/Customer/form.html")
    
    firstNameInput = driver.find_element_by_id("first-name")
    lastNameInput = driver.find_element_by_id("last-name")
    ageInput = driver.find_element_by_id("age")
    submitButton = driver.find_element_by_id("sub")
    
    firstNameInput.send_keys("johnjohn")
    lastNameInput.send_keys("canoncan")
    ageInput.send_keys("0")

    # Submit the form
    submitButton.click()
    
    take_screenshot(driver, "test_case10.png")
    
    result = driver.find_element_by_id("formname").text
    assert result == "Customer Detail Form"
    
    driver.close()

def test_case11():
    driver = webdriver.Chrome(executable_path="D:\\webdriver\\chromedriver.exe")
    driver.get("http://localhost/Customer/form.html")
    
    firstNameInput = driver.find_element_by_id("first-name")
    lastNameInput = driver.find_element_by_id("last-name")
    ageInput = driver.find_element_by_id("age")
    submitButton = driver.find_element_by_id("sub")
    
    firstNameInput.send_keys("johnjohn")
    lastNameInput.send_keys("canoncan")
    ageInput.send_keys("151")

    # Submit the form
    submitButton.click()
    
    take_screenshot(driver, "test_case11.png")
    
    result = driver.find_element_by_id("formname").text
    assert result == "Customer Detail Form"
    
    driver.close()

if __name__ == "__main__":
    test_case1()
    test_case2()
    test_case3()
    test_case4()
    test_case5()
    test_case6()
    test_case8()
    test_case10()
    test_case11()
