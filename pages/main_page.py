from .base_page import BasePage
from selenium.webdriver.common.by import By

class Locators:
    SEARCH_FIELD = (By.ID, "text")
    SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    SUGGESTION_LIST = (By.CLASS_NAME, "mini-suggest__popup_visible")
    RESULTS_LIST = (By.CSS_SELECTOR, "#search-result > .serp-item a.link > b")
    IMAGES_LINK = (By.XPATH, '//*[@data-id="images"]')
    FIRST_CATEGORY = (By.CLASS_NAME, "PopularRequestList-Item_pos_0")
    IMAGES_SEARCH_FIELD = (By.NAME, "text")
    FIRST_IMAGE = (By.CLASS_NAME, "serp-item_pos_0")
    NEXT_IMAGE_BUTTON = (By.CLASS_NAME, "CircleButton_type_next")
    PREVIOUS_IMAGE_BUTTON = (By.CLASS_NAME, "CircleButton_type_prev")
    CURRENT_IMAGE = (By.CLASS_NAME, "MMImage-Origin")

class MainPage(BasePage):

    def should_be_search_field(self):
        assert self.is_element_present(*Locators.SEARCH_FIELD), "Search field is not presented"

    def should_be_suggestion_list(self):
        assert self.is_element_present(*Locators.SUGGESTION_LIST), "Suggestion list is not presented"

    def should_be_images_link(self):
        assert self.is_element_present(*Locators.IMAGES_LINK), "Images link is not presented"

    def enter_word(self, word):
        search_field = self.browser.find_element(*Locators.SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.browser.find_element(*Locators.SEARCH_BUTTON).click()

    def go_to_images_page(self):
        link = self.browser.find_element(*Locators.IMAGES_LINK)
        link.click()
        
    def search_for_tensor(self):
        results = self.browser.find_elements(*Locators.RESULTS_LIST)
        items = [elem.text.strip() for elem in results[:5]]
        if "tensor.ru" not in items:
            raise Exception('tensor.ru is not presented in first 5 results')