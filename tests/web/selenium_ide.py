from selenium import webdriver
from selenium.webdriver.common.by import By


class TestComprarPassagem:
    def setup_method(self):
        self.driver = webdriver.Chrome(
            'C:\\Users\Windows 10\\PycharmProjects\\134inicial\\vendors\\drivers\\chromedriver102.exe'
        )
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_comprar_passagem(self):
        self.driver.get("https://blazedemo.com/")
        self.driver.set_window_size(1296, 696)
        self.driver.find_element(By.NAME, "FromPort").click()
        dropdown = self.driver.find_element(By.NAME, "fromPort")
        dropdown.find_element(By.XPATH, "//option[. = 'São Paolo']").click()
        self.driver.find_element(By.NAME, "toPort").click()
        dropdown = self.driver.find_element(By.NAME, "toPort")
        dropdown.find_element(By.XPATH, "//option[. = 'New York'").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "h3").text == "Flights from São Paolo to New York:"
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1).btn").click()
        self.driver.find_element(By.ID, "inputName").click()
        self.driver.find_element(By.ID, "inputName").send_keys("Juca")
        self.driver.find_element(By.ID, "address").click()
        self.driver.find_element(By.ID, "cardType").click()
        dropdown = self.driver.find_element(By.ID, "cardType")
        dropdown.find_element(By.ID, "//option[. = American Express']").click()
        self.driver.find_element(By.ID, "rememberMe").click()
        self.driver.find_element(By.CSS_SELECTOR, "btn-primary").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "h1").text == "Thank you for your purchase today!"
        assert self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) >td:nth-child(2)").text == "555 USD"
