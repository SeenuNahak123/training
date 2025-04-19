from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


# dropdown_element = driver.find_element(By.ID, "dropdown")

# # Step 3: Create a Select object
# dropdown = Select(dropdown_element)

# # Step 4: Select "Option 2" by visible text
# dropdown.select_by_visible_text("Option 2")



class sort:
    def __init__(self,driver):
        self.driver=driver
        self.dropdown_element=(By.XPATH, "//*[@id=\"header_container\"]/div[2]/div/span/select")
    
    def sort_dropdown(self,user_dropdown):
        dropdown=Select(self.dropdown_element)
        dropdown.select_by_visible_text(user_dropdown)

