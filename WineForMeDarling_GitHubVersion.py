from selenium import webdriver
from selenium.webdriver.common.by import By
from win10toast import ToastNotifier

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

    toast = ToastNotifier()

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

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
    
    if "בהצלחה" in value:
        toast.show_toast(title = "WineForMeDarling", msg = "Success!", duration = 20, icon_path = None,)
    else:
        toast.show_toast(title = "WineForMeDarling", msg = "Failed!", duration = 20, icon_path = None,)



    driver.quit()


if __name__ == "__main__":
     loadMyWines()

