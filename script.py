import org.sikuli.script.SikulixForJython
import sys
import pytest
import allure
from selenium import webdriver
from sikuli import *
from allure_commons.types import AttachmentType
import time


@pytest.fixture
def create_driver():
    return webdriver.Chrome()
    


def fail_routine_1(exception):
      screen = Screen()
      file = screen.capture(screen.getBounds())
      allure.attach(exception)
      pytest.fail(exception)     

@pytest.mark.ex1
def test_verify_home_location(create_driver):
     driver = create_driver 
     driver.get("https://www.google.com/maps")
     driver.maximize_window()
     try:
         Settings.MinSimilarity = 0.9 



         page_load = "/Users/santosmac/TestAutomtionLab/sikuli_poc/images/page_load_done"
         makati  = "/Users/santosmac/TestAutomtionLab/sikuli_poc/images/makati"
         verify = "/Users/santosmac/TestAutomtionLab/sikuli_poc/images/verify"
         makati  = "/Users/santosmac/TestAutomtionLab/sikuli_poc/images/makati"
         verify = "/Users/santosmac/TestAutomtionLab/sikuli_poc/images/verify"
         zoom = "/Users/santosmac/TestAutomtionLab/sikuli_poc/images/zoom_plus"
         reference = "/Users/santosmac/TestAutomtionLab/sikuli_poc/images/refresh_ref"
         tab = "/Users/santosmac/TestAutomtionLab/sikuli_poc/images/tab"
                 
         ref_pattern = Pattern(reference)  
         center = ref_pattern.targetOffset(558,415)         
         makati_a = Pattern(makati)
         makati_a.targetOffset(-20,20)
         wait(tab) 
         click(tab) 
         ##wait(page_load,10)
         wait(makati_a,10)
         time.sleep(1)
         hover(makati_a)
         mouseDown(Button.LEFT)
         hover(center)
         mouseUp(Button.LEFT)

     except FindFailed as e:
         fail_routine_1(e)

def test_tc_1():
      try:
         click("/Users/santosmac/TestAutomtionLab/sikuli_poc/images/object1.png")
         click("/Users/santosmac/TestAutomtionLab/sikuli_poc/images/object2.png")
         wait("/Users/santosmac/TestAutomtionLab/sikuli_poc/images/object.png",10) 
      except FindFailed as e:
         fail_routine_1(e)
