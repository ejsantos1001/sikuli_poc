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
     driver.get("https://www.google.com/maps/@14.5500324,121.0242512,19z")
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
         y_m = "/Users/santosmac/TestAutomtionLab/sikuli_poc/images/yellow_man"
         coffee_bean = "/Users/santosmac/TestAutomtionLab/sikuli_poc/images/coffee_bean"
         garden ="/Users/santosmac/TestAutomtionLab/sikuli_poc/images/garden_towers"
         rotate ="/Users/santosmac/TestAutomtionLab/sikuli_poc/images/rotate"

         """ref_pattern = Pattern(reference)
         center = ref_pattern.targetOffset(526,380)
         makati_a = Pattern(makati)
         makati_a.targetOffset(0,20)
         makati_b = Pattern(makati)
         makati_b.targetOffset(0,60)"""
         wait(tab)
         click(tab)

         ##wait(makati_a,10)
         """mouseMove(makati_a)
         mouseDown(Button.LEFT)
         mouseMove(center)
         mouseUp(Button.LEFT)
         mouseMove(makati)

         time.sleep(1)
         wheel(makati_b,WHEEL_DOWN,30)"""
         g_t = Pattern(garden)
         dx_meters = -37.53
         dy_meters = -58.60
         factor = 0.298

         dx_pix = int(dx_meters * 1/factor)
         dy_pix = int(dy_meters * 1/factor)

         condo = g_t.targetOffset(dx_pix,dy_pix)

         time.sleep(2)
         drag(y_m)
         dropAt(condo)
         wait(tab)
         click(tab)

         for _ in range(4):
             wait(rotate,5)
             click(rotate)
             v = None
             v = exists(verify,5)
             v.highlight(2)
             if (v is not None):
                 break


     except FindFailed as e:
         fail_routine_1(e)

def test_tc_1():
      try:
         click("/Users/santosmac/TestAutomtionLab/sikuli_poc/images/object1.png")
         click("/Users/santosmac/TestAutomtionLab/sikuli_poc/images/object2.png")
         wait("/Users/santosmac/TestAutomtionLab/sikuli_poc/images/object.png",10)
      except FindFailed as e:
         fail_routine_1(e)
