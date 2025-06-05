import logging
from selenium import webdriver
from pages import UrbanRoutesPage
from data import URBAN_ROUTES_URL, ADDRESS_FROM, ADDRESS_TO, PHONE_NUMBER, CARD_NUMBER, CARD_EXPIRY_DATE, CARD_CVV, MESSAGE_FOR_DRIVER
import helpers  # Assuming helpers.py has server check functions

# Set up logging
logging.basicConfig(level=logging.INFO)

class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        from selenium.webdriver.chrome.options import Options

        # Set Chrome options
        chrome_options = Options()
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)

        # Check server connectivity
        # Add in S8
        # Assuming helpers.py has a function check_server_availability(url)
        try:
            helpers.check_server_availability(URBAN_ROUTES_URL)
            print(f"Server {URBAN_ROUTES_URL} is reachable.")
        except Exception as e:
            print(f"Server check failed: {e}")

    def test_set_route(self):
        self.driver.get(URBAN_ROUTES_URL)  # Open the URL for this test
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_address(ADDRESS_FROM, ADDRESS_TO)  # Set 'from' and 'to' addresses
        assert routes_page.get_from() == ADDRESS_FROM, f"Expected {ADDRESS_FROM}, but got {routes_page.get_from()}"
        assert routes_page.get_to() == ADDRESS_TO, f"Expected {ADDRESS_TO}, but got {routes_page.get_to()}"

    def test_select_plan(self):
        self.driver.get(URBAN_ROUTES_URL)  # Open the URL for this test
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_supportive_plan()  # Select the 'Supportive' plan
        assert routes_page.get_selected_tariff() == "Supportive", f"Expected 'Supportive', but got {routes_page.get_selected_tariff()}"

    def test_fill_phone_number(self):
        self.driver.get(URBAN_ROUTES_URL)  # Open the URL for this test
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.fill_phone_number(PHONE_NUMBER)  # Fill the phone number
        assert routes_page.get_phone_number() == PHONE_NUMBER, f"Expected {PHONE_NUMBER}, but got {routes_page.get_phone_number()}"

    def test_fill_card(self):
        self.driver.get(URBAN_ROUTES_URL)  # Open the URL for this test
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_credit_card(CARD_NUMBER, CARD_EXPIRY_DATE, CARD_CVV)  # Add the credit card details
        assert routes_page.get_card_number() == CARD_NUMBER, f"Expected card number {CARD_NUMBER}, but got {routes_page.get_card_number()}"

    def test_comment_for_driver(self):
        self.driver.get(URBAN_ROUTES_URL)  # Open the URL for this test
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.write_driver_comment(MESSAGE_FOR_DRIVER)  # Write a comment for the driver
        assert routes_page.get_comment() == MESSAGE_FOR_DRIVER, f"Expected comment '{MESSAGE_FOR_DRIVER}', but got {routes_page.get_comment()}"

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        # Placeholder for ordering blanket and handkerchiefs
        print("Testing order: blanket and handkerchiefs")
        pass

    def test_order_2_ice_creams(self):
        # Add in S8
        # Placeholder for ordering 2 ice creams
        print("Testing order: 2 ice creams")
        pass

    def test_car_search_model_appears(self):
        # Add in S8
        # Placeholder for car search model appearance check
        print("Testing car search model appears")
        pass

    @classmethod
    def teardown_class(cls):
        logging.info("Closing the browser.")
        cls.driver.quit()
