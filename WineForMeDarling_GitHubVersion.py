import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def loadMyWines():

    info = { 
        'url': 'https://wine-he.com/',
        'name': 'your name',
        'phone': 'your phone',
        'email': 'your email',
        'sum': 0,
        'card': 'tenbis',
        'card_number': 0
    }

    driver = webdriver.Chrome()

    driver.get(info['url'])

    driver.implicitly_wait(2)

    nameField = driver.find_element(By.ID, "form-field-name") # text
    phoneField = driver.find_element(By.ID, "form-field-field_3a7272e") # text
    emailField = driver.find_element(By.ID, "form-field-email") # text
    sumField = driver.find_element(By.ID, "form-field-field_140acd2") # text
    card_field = driver.find_element(By.ID, "form-field-field_2eb71e4-0") # choose one
    cardNumberField = driver.find_element(By.ID, "form-field-field_cad2223") # text
    submit_button = driver.find_element(by=By.CLASS_NAME, value="elementor-button") # button

    nameField.send_keys(info['name'])
    phoneField.send_keys(info['phone'])
    emailField.send_keys(info['email'])
    sumField.send_keys(info['sum'])
    card_field.click()
    cardNumberField.send_keys(info['card_number'])
    submit_button.click()

    driver.implicitly_wait(2)

    message = driver.find_element(by=By.CLASS_NAME, value="elementor-message-success")
    value = message.text
    assert "בהצלחה" in value

    driver.quit()


# Main script to run daily at 10 AM
while True:
    current_time = time.localtime()

    # Check if it's 10 AM
    if current_time.tm_hour == 10 and current_time.tm_min == 0:
            loadMyWines()
            print("Wines loaded at 10 AM for")

    # Sleep for 1 minute and check again
    time.sleep(60)


