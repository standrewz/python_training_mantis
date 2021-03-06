from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.soap import SoapHelper

class Application:

    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.soap = SoapHelper(self)
        self.config = config
        self.base_url = config["web"]["baseUrl"]
        self.login = config['webadmin']['username']
        self.password = config['webadmin']['password']

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def return_to_home_page(self):
        wd = self.wd
        if not (wd.current_url == self.base_url):
            wd.find_element_by_link_text("My View").click()

    def destroy(self):
        self.wd.quit()