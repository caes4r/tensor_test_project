from .base_page import BasePage
from .main_page import Locators
import time

class ImagesPage(BasePage):

    def should_be_images_url(self):
        assert "yandex.ru/images" in self.browser.current_url, "Images URL is not presented"

    def go_to_first_category(self):
        elem = self.browser.find_element(*Locators.FIRST_CATEGORY)
        attr_value = elem.get_attribute("data-grid-text")
        elem.click()
        time.sleep(2)
        attr_value2 = self.browser.find_element(*Locators.IMAGES_SEARCH_FIELD)
        assert attr_value in attr_value2.get_attribute("value"), "Wrong category name"

    def go_to_first_image(self):
        image = self.browser.find_element(*Locators.FIRST_IMAGE)
        image.click()

    def go_to_next_and_previous_image(self):
        button_next = self.browser.find_element(*Locators.NEXT_IMAGE_BUTTON)
        current_image = self.browser.find_element(*Locators.CURRENT_IMAGE)
        attr_value_1 = current_image.get_attribute("src")
        button_next.click()
        button_prev = self.browser.find_element(*Locators.PREVIOUS_IMAGE_BUTTON)
        button_prev.click()
        current_image = self.browser.find_element(*Locators.CURRENT_IMAGE)
        time.sleep(2)
        attr_value_2 = current_image.get_attribute("src")
        time.sleep(2)
        assert attr_value_1 == attr_value_2, "Wrong image"

    def go_to_previous_image(self):
        button = self.browser.find_element(*Locators.PREVIOUS_IMAGE_BUTTON)
        button.click()

    
