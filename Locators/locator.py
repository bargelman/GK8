from selenium.webdriver.common.by import By


class Locators:
    JSON_BUTTON = (By.XPATH, "(//button[normalize-space()='JSON'])[1]")
    JSON_TEXT_FIELD = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/main[1]/div[1]/div[1]/section[1]/section[1]/div"
                                 "[3]/div[2]/div[1]/div[1]/div[1]/pre[1]")

