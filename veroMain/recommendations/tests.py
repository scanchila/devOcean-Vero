from django.test import TestCase

from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select

class UserLogin(StaticLiveServerTestCase):

  def testLogin(self):
    driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
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




    '''Ingresar a Recomendaciones'''

    driver.get(self.live_server_url+'/recommendations/recommendations/')
    submit = driver.find_element_by_id('BotonFinalizarSesion')
    time.sleep(2)
    submit.click()
    time.sleep(2)

    '''Ingresar a formulario recomendaciones'''
    

    nombre = driver.find_element_by_id('nombre')
    select = Select(driver.find_element_by_id('tipo'))

    # select by visible text
    select.select_by_visible_text('Película')

    # select by value 
    select.select_by_value('film')

    
    descripcion = driver.find_element_by_id('descripcion')
    Genero =driver.find_element_by_id('genero')
    submit = driver.find_element_by_id('boton')

    nombre.send_keys('Lágrimas de Ángeles')
    descripcion.send_keys('Linda Película')
    Genero.send_keys('Drama')
    time.sleep(2)
    submit.send_keys(Keys.RETURN)
    time.sleep(2)
    
    


    assert 'Recomendación del momento' in driver.page_source