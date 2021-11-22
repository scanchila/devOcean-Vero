from django.test import TestCase

from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# Create your tests here.
class CreateUser(StaticLiveServerTestCase):

  def testSuccessCreate(self):
    driver = webdriver.Chrome(executable_path="C:\\ll\\chromedriver.exe")
    print(self.live_server_url)
    driver.get(self.live_server_url+'/users/register/')


    username = driver.find_element_by_id('id_username')
    password1 = driver.find_element_by_id('id_password1')
    password2 =driver.find_element_by_id('id_password2')
    email = driver.find_element_by_id('id_email')
    submit = driver.find_element_by_id('Registrar')
    terminos = driver.find_element_by_name('terminos')


    username.send_keys('TestUser1')
    password1.send_keys('Testpassword123')
    email.send_keys('test@test.com')
    terminos.click()
    password2.send_keys('Testpassword123')
    time.sleep(1)
    submit.send_keys(Keys.RETURN)
    time.sleep(2)


    assert 'Iniciar ses' in driver.page_source



#Excepcion
class UserAlreadyCreated(StaticLiveServerTestCase):

  def testFailCreate(self):
    driver = webdriver.Chrome(executable_path="C:\\ll\\chromedriver.exe")
    print(self.live_server_url)
    driver.get(self.live_server_url+'/users/register/')
    assert 'user with that username already' not in driver.page_source
    username = driver.find_element_by_id('id_username')
    password1 = driver.find_element_by_id('id_password1')
    password2 =driver.find_element_by_id('id_password2')
    email = driver.find_element_by_id('id_email')
    submit = driver.find_element_by_id('Registrar')
    terminos = driver.find_element_by_name('terminos')


    username.send_keys('TestUser1')
    password1.send_keys('Testpassword123')
    email.send_keys('test@test.com')
    terminos.click()
    password2.send_keys('Testpassword123')
    time.sleep(1)
    submit.send_keys(Keys.RETURN)
    time.sleep(2)

    assert 'user with that username already' not in driver.page_source

    driver.get(self.live_server_url+'/users/register/')

    username = driver.find_element_by_id('id_username')
    password1 = driver.find_element_by_id('id_password1')
    password2 =driver.find_element_by_id('id_password2')
    email = driver.find_element_by_id('id_email')
    submit = driver.find_element_by_id('Registrar')
    terminos = driver.find_element_by_name('terminos')


    username.send_keys('TestUser1')
    password1.send_keys('Testpassword123')
    email.send_keys('test@test.com')
    terminos.click()
    password2.send_keys('Testpassword123')
    time.sleep(1)
    submit.send_keys(Keys.RETURN)
    time.sleep(2)

    assert 'user with that username already' in driver.page_source


#Excepcion
class IncorrectEmail(StaticLiveServerTestCase):

  def testFailCreate(self):
    driver = webdriver.Chrome(executable_path="C:\\ll\\chromedriver.exe")
    print(self.live_server_url)
    driver.get(self.live_server_url+'/users/register/')
    username = driver.find_element_by_id('id_username')
    password1 = driver.find_element_by_id('id_password1')
    password2 =driver.find_element_by_id('id_password2')
    email = driver.find_element_by_id('id_email')
    submit = driver.find_element_by_id('Registrar')
    terminos = driver.find_element_by_name('terminos')


    username.send_keys('TestUser1')
    password1.send_keys('Testpassword123')
    email.send_keys('testAttest.com')
    terminos.click()
    password2.send_keys('Testpassword123')
    time.sleep(1)
    submit.send_keys(Keys.RETURN)
    time.sleep(2)

    assert 'Acepto los terminos' not in driver.page_source

   


class UserLogin(StaticLiveServerTestCase):

  def testLogin(self):
    driver = webdriver.Chrome(executable_path="C:\\ll\\chromedriver.exe")
    print(self.live_server_url)
    driver.get(self.live_server_url+'/users/register/')
    username = driver.find_element_by_id('id_username')
    password1 = driver.find_element_by_id('id_password1')
    password2 =driver.find_element_by_id('id_password2')
    email = driver.find_element_by_id('id_email')
    submit = driver.find_element_by_id('Registrar')
    terminos = driver.find_element_by_name('terminos')


    username.send_keys('TestUser1')
    password1.send_keys('Testpassword123')
    email.send_keys('test@test.com')
    terminos.click()
    password2.send_keys('Testpassword123')
    time.sleep(1)
    submit.send_keys(Keys.RETURN)
    time.sleep(2)


    username = driver.find_element_by_id('id_username')
    password = driver.find_element_by_id('id_password')

    password.send_keys('Testpassword123')
    username.send_keys('TestUser1')
    submit = driver.find_element_by_id('Registrar')
    submit.click()

    time.sleep(2)

    assert 'Recomendación del momento' in driver.page_source
