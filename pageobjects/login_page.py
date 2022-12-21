import time

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select


from base.base_driver import BaseDriver


class login(BaseDriver):
    username_name="userName"
    password_name="password"
    submit_name="submit"
    signoff_link ="SIGN-OFF"

    def __init__(self, driver):
        self.driver = driver


    def  setusername(self, username, password):
        self.driver.find_element(By.NAME, self.username_name).send_keys(username)
        self.driver.find_element(By.NAME, self.password_name).send_keys(password)

    # time.sleep(5)
        self.driver.find_element(By.NAME, self.submit_name).click()

    def pagetitle(self):
        ptitle = self.driver.title
        # print(ptitle)
        return ptitle

    def signoff(self):
        self.driver.find_element(By.LINK_TEXT, self.signoff_link).click()