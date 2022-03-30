from email.mime import image
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.images_page import ImagesPage
import time

def test_search(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_search_field()
    page.enter_word("тензор")
    page.should_be_suggestion_list()
    page.click_on_the_search_button()
    page.search_for_tensor()

def test_search_images(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_images_link()
    page.go_to_images_page()
    browser.switch_to.window(browser.window_handles[1])
    images_page = ImagesPage(browser, browser.current_url)
    images_page.should_be_images_url()
    images_page.go_to_first_category()
    images_page.go_to_first_image()
    images_page.go_to_next_and_previous_image()
    time.sleep(10)