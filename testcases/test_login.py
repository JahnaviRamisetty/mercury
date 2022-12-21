import datetime
import os
import time
import pytest
from pageobjects.login_page import login
from utilites import XLutilities
from utilites.readproperities import ReadConfig
#from utilites.customlogger import LogGen
@pytest.mark.login
#@pytest.fixture(scope="function")
class Test_login():
    URL = ReadConfig.getApplicationURL()
    # user = ReadConfig.getusername()
    # pwd = ReadConfig.getpassword()


    @pytest.mark.login
    #@pytest.fixture(scope="function")
    def test_logintopage(self,setup):
        self.driver = setup
        self.driver.get(self.URL)
        # btitle=self.driver.title
        # print(btitle)

        self.lp = login(self.driver)
        time.sleep(2)
        # self.lp.setusername(self.user,self.pwd)

        path = "C:\\new\\login_testdata.xlsx"
        rows = XLutilities.getRowCount(path, 'Sheet1')
        for r in range(2, rows + 1):  # starts from 2 row
            # extract data from each column
            username = XLutilities.readData(path, 'Sheet1', r, 1)
            password = XLutilities.readData(path, 'Sheet1', r, 2)
            self.lp.setusername(username, password)
            act_title = self.lp.pagetitle()
            expect_title = "Login: Mercury Tours"
            num = str(datetime.datetime.now())
            repchar = [" ", "-", ".", ":"]
            for char in repchar:
                num = num.replace(char, "")
            print(num)
            # print(num)
            if act_title == expect_title:

                img_name = "pass" + num + ".png"
                img_path = os.path.join("C:\\new", img_name)
                self.driver.save_screenshot(img_path)
                print("successfully login")
                XLutilities.writeData(path, 'Sheet1', r, 3, "test passed")
                self.lp.signoff()
            else:
                XLutilities.writeData(path, 'Sheet1', r, 3, "test failed")
                img_name = "fail" + num + ".png"
                img_path = os.path.join("C:\\new", img_name)
                self.driver.save_screenshot(img_path)
                print("FAILED")
                self.driver.refresh()

