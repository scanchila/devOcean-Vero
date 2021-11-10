from django.test import TestCase

from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
# Create your tests here.
class ActivityGrupal(StaticLiveServerTestCase):
  
  
  def testFilterActivity(self):
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

    driver.get(self.live_server_url+'/myActivities/grupalActivities/')
    activitiName=driver.find_element_by_name('nombre')
    activitiType=Select(driver.find_element_by_id('tipo'))
    activitiDescription=driver.find_element_by_name('descripcion')
    activitiDuration=driver.find_element_by_name('duracion')
    activitiDate=driver.find_element_by_name('fecha')
    activitihour=driver.find_element_by_name('hora')
    activitimax=driver.find_element_by_name('maximo')
    activitiaddres=driver.find_element_by_name('direccion')
    activitiemail=driver.find_element_by_name('email')
    submit2 = driver.find_element_by_id('SubmitCreate')



    activitiName.send_keys('Danza Forclorica')
    time.sleep(2)
    activitiType.select_by_visible_text('folclor')
    time.sleep(2)
    activitiDescription.send_keys('Danza muy divertida')
    time.sleep(2)
    activitiDuration.send_keys('00:30:00')
    time.sleep(2)
    activitiDate.send_keys('10/11/2021')
    time.sleep(2)
    activitihour.send_keys('07:02a. m.')
    time.sleep(2)
    activitimax.send_keys('10')
    time.sleep(2)
    activitiaddres.send_keys('Carrera 60')
    time.sleep(2)
    activitiemail.send_keys('pepito@perez.com')
    time.sleep(2)
    
    submit2.send_keys(Keys.RETURN)
    time.sleep(2)

    driver.get(self.live_server_url+'/myActivities/filtroActividadesgrupales/')
    
    select = Select(driver.find_element_by_name('time'))
    submit = driver.find_element_by_id('btnFiltro')
    
    select.select_by_value('any')
    time.sleep(1)
    submit.send_keys(Keys.RETURN)
    


    assert 'Actividades Grupales' in driver.page_source
