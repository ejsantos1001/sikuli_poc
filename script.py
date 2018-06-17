import org.sikuli.script.SikulixForJython
import sys
import pytest
import allure
from sikuli import *
from allure_commons.types import AttachmentType

def fail_routine_1(exception):
      screen = Screen()
      file = screen.capture(screen.getBounds())
      allure.attach('test',file,type=AttachmentType.PNG)
      pytest.fail(exception)     


def test_tc_1():
      try:
         click("/Users/santosmac/TestAutomtionLab/sikuli_poc/images/object1.png")
         click("/Users/santosmac/TestAutomtionLab/sikuli_poc/images/object2.png")
         wait("/Users/santosmac/TestAutomtionLab/sikuli_poc/images/object.png",10) 
      except FindFailed as e:
         fail_routine_1(e)
