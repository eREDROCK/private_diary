from django.test import LiveServerTestCase
from django.urls import reverse_lazy
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

# Create your tests here.

class TestLogin(LiveServerTestCase): 
    @classmethod
    def setUpClass(cls):
      super().setUpClass()
      cls.selenium=WebDriver(executable_path='C:Users\rdrc1\chromedriver_win32')

    @classmethod
    def tearDownClass(cls):
       cls.selenium.quit()
       super().tearDownClass()
    
    def test_login(self):
       self.selenium.get('http://localhost:8000' + str(reverse_lazy('account_login')))

       username_input=self.selenium.find_element(By.NAME, "login")
       username_input.send_keys('rdrc136@gmail.com')
       password_input=self.selenium.find_element(By.NAME, "password")
       password_input.send_keys('1204noShiru')
       self.selenium.find_element(By.CLASS_NAME, "btn").click()

       self.assertEqual('日記一覧|Private Diary', self.selenium.title)

