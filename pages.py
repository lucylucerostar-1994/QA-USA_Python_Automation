# pages.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    phone_field = (By.XPATH, '//input[@placeholder="Phone number"]')
    card_number_field = (By.XPATH, '//input[@placeholder="Card number"]')
    card_code_field = (By.XPATH, '//input[@placeholder="Card code"]')  # Adjust if your field is named 'Card code'
    comment_field = (By.XPATH, '//textarea[@placeholder="Comment for the driver"]')

    # Methods
    def set_address(self, address_from, address_to):
        from_input = self.driver.find_element(*self.from_field)
        from_input.clear()
        from_input.send_keys(address_from)
        to_input = self.driver.find_element(*self.to_field)
        to_input.clear()
        to_input.send_keys(address_to)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_attribute("value")

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_attribute("value")

    def get_phone_number(self):
        return self.driver.find_element(*self.phone_field).get_attribute("value")

    def get_card_number(self):
        return self.driver.find_element(*self.card_number_field).get_attribute("value")

    def get_card_code(self):
        return self.driver.find_element(*self.card_code_field).get_attribute("value")

    def get_comment(self):
        return self.driver.find_element(*self.comment_field).get_attribute("value")

    def select_supportive_plan(self):
        supportive_plan_option = (By.XPATH, '//div[contains(@class, "tariff") and contains(text(), "Supportive")]')
        selected_tariff = (By.CLASS_NAME, 'is-selected')
        self.driver.find_element(*supportive_plan_option).click()
        self.wait.until(
            EC.text_to_be_present_in_element(selected_tariff, "Supportive")
        )

    def get_selected_tariff(self):
        selected_tariff = (By.CLASS_NAME, 'is-selected')
        return self.driver.find_element(*selected_tariff).text

    def fill_phone_number(self, phone_number):
        phone_input = self.driver.find_element(*self.phone_field)
        phone_input.clear()
        phone_input.send_keys(phone_number)

    def add_credit_card(self, card_number, card_code):
        card_input = self.driver.find_element(*self.card_number_field)
        card_input.clear()
        card_input.send_keys(card_number)
        code_input = self.driver.find_element(*self.card_code_field)
        code_input.clear()
        code_input.send_keys(card_code)

    def write_driver_comment(self, comment):
        comment_input = self.driver.find_element(*self.comment_field)
        comment_input.clear()
        comment_input.send_keys(comment)

