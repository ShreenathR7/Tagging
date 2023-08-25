# app.py - The main executable file
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
from Test_locators import locators
from Test_data import data
import pytest


class Test_Logimax:
    @pytest.fixture
    

    def booting_function(self):
       self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
       self.driver.get(data.Logi_Data().url)
       self.driver.maximize_window()
       self.driver.implicitly_wait(5)
  
  
    def test_vendor_registration(self,booting_function):   
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
        sleep(8)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click()
        sleep(8)
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT,value=locators.Logi_Locators().Inventory_module).click()
        sleep(5)
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT,value=locators.Logi_Locators().Tagging).click()
        sleep(6)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Add_tagging).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().lot_no).click()
        sleep(5)
        lot = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        lot.send_keys('7959')
        lot.send_keys(Keys.RETURN) 
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().product).click()
        sleep(5)
        product = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        product.send_keys('RING & COIN-GB')
        product.send_keys(Keys.RETURN) 
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().section).click()
        sleep(5)
        section = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        section.send_keys('GOLD PENDANT-GP')
        section.send_keys(Keys.RETURN) 
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().design).click()
        sleep(5)
        design = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        design.send_keys('ARAM')
        design.send_keys(Keys.RETURN) 
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().sub_design).click()
        sleep(5)
        design = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        design.send_keys('SOLID CHAIN')
        design.send_keys(Keys.RETURN) 
        sleep(5)
        number = 35
        gross_wgt = self.driver.find_element(by=By.ID,value=locators.Logi_Locators().gross_wt)
        gross_wgt.send_keys(number)  
        sleep(5)
        #self.driver.find_element(by=By.ID,value=locators.Logi_Locators().HUID).send_keys(data.Logi_Data.huid_no)
        #sleep(5)
        #self.driver.find_element(by=By.ID,value=locators.Logi_Locators().HUID1).send_keys(data.Logi_Data.huid1_No)
        #sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().certificate_no).send_keys(data.Logi_Data.certificate_No)
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().manuf_code).send_keys(data.Logi_Data.manufacture_code)
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().style_code).send_keys(data.Logi_Data.Style_Code)
        sleep(5)
        number_1 = '5000'
        cost=self.driver.find_element(by=By.ID,value=locators.Logi_Locators().purchase_cost)
        cost.send_keys(number_1)
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().add_copy).click()
        assert self.driver.title == 'Logimax Technology | Admin'
        print("SUCCESS : Tagging  added successfully lot_no : {a}, product: {b},section : {c},design:{d},sub_design{e},gross_wt{f},certificate_no{g},manuf_code : {h},style_code : {i},purchase_cost{j}". format(a = '7959', b= 'RING & COIN-GB', c='GOLD PENDANT-GP', d='ARAM', e='SOLID CHAIN', f=number, g=data.Logi_Data.certificate_No, h=data.Logi_Data.manufacture_code, i=data.Logi_Data.Style_Code,j = number_1))
     
        
        