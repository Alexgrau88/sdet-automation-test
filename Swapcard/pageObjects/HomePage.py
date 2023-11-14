from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    hamburger_menu = (By.ID, "nav-hamburger-menu")
    arts_and_crafts = (By.XPATH, "//div[contains(text(),'Arts & Crafts')]")
    beading_jewelry_making_1 = (By.XPATH, "//a[contains(text(),'Beading & Jewelry Making')]")
    arts_crafts_sewing = (By.XPATH, "//span[contains(text(),'Arts, Crafts & Sewing')]")
    beading_jewelry_making_2 = (By.XPATH, "//span[contains(text(),'Beading & Jewelry Making')]")
    engraving_machines_tools = (By.XPATH, "//span[contains(text(),'Jewelry Making Engraving Machines & Tools')]")
    price_sort_dropdown = (By.CLASS_NAME, "a-dropdown-container")
    price_dropdown_value = (By.ID, "s-result-sort-select_2")
    third_available_item = (By.XPATH, "(//div[@data-asin])[4]/div/div")
    review_score = (By.XPATH, "//a/span[@class='a-size-base a-color-base'][1]")
    item_price = (By.XPATH, "//span[@class='a-price-whole']")

    def get_hamburger_menu(self):
        return self.driver.find_element(*HomePage.hamburger_menu)

    def get_arts_and_crafts(self):
        return self.driver.find_element(*HomePage.arts_and_crafts)

    def get_beading_jewelry_making_1(self):
        return self.driver.find_element(*HomePage.beading_jewelry_making_1)

    def get_arts_crafts_sewing(self):
        return self.driver.find_element(*HomePage.arts_crafts_sewing)

    def get_beading_jewelry_making_2(self):
        return self.driver.find_element(*HomePage.beading_jewelry_making_2)

    def get_engraving_machines_tools(self):
        return self.driver.find_element(*HomePage.engraving_machines_tools)

    def get_price_sort_dropdown(self):
        return self.driver.find_element(*HomePage.price_sort_dropdown)

    def get_price_dropdown_value(self):
        return self.driver.find_element(*HomePage.price_dropdown_value)

    def get_third_available_item(self):
        return self.driver.find_element(*HomePage.third_available_item)

    def get_review_score(self):
        return self.driver.find_element(*HomePage.review_score)

    def get_item_price(self):
        return self.driver.find_element(*HomePage.item_price)

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)