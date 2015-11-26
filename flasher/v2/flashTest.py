# -*- coding: utf-8 -*-

from flasher.usb import USB,wait_for_usb
import unittest
import logging
import sys
from functools import wraps
import time
import unittest
from observable_test import state
# from observed import observable_method
from utils import CommandRunner

log = logging.getLogger("serial")
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


class Upload(unittest.TestCase):
    
    stateNames = { "test_00_dummy":"Dummy...\ndum",
                  "test_00_dummy2":"Dummy2...\ndum",
                  "test_01_flash":"Uploading...\n正在加载固件",
                  }
    label="LAB"
    color=[0.75,     0.25,    0,    1] #this is a GUI property and shouldn't really be here
    
    err_codes = {
        -1: "Unknown Failure",
        128: "FEL Error.",
        129: "DRAM Error?",
        130: "Upload Error.",
        131: "Upload Error.",
        132: "Bad Cable?",
        133: "Fastboot fail.",
        134: "Fastboot fail.",
        135: "Bad U-boot."
    }
    
    
    def setUp(self):
#        print("Waiting for USB")
#         if not wait_for_usb( instance=None, type="fel", log=log, timeout=30 ):
#             raise Exception( "Flashing failed: ", "Could not find FEL device" )
        pass  
    
    def test_00_dummy(self):    
        time.sleep(6)
#         raise Exception(" fail after 6 seconds","fail")

    def test_00_dummy2(self):    
        time.sleep(6)
        raise Exception(" fail after 6 seconds","fail")

    #unit test    
#     @state("State test_flash")
    def atest_01_flash(self):
        print("Running chip-fel-flash")
        commandRunner = CommandRunner(log)
        errcode = commandRunner.call_and_return(cmd=["./chip-fel-flash.sh", "-f"], timeout=400 )
        print("Error code: " + str(errcode) )
        if errcode != 0:
            if not errcode in self.err_codes:
                errcode = -1
            raise Exception( "Flashing failed: ", self.err_codes[ errcode ] )

        

#         
# class TestHardware(ObservableTestCase):
#     
#     def setUp(self):
#         print("Waiting for USB")
#         
#         if not wait_for_usb( instance=Null, type="fel", log=log, timeout=30 ):
#             raise Exception( "Flashing failed: ", "Could not find FEL device" )
#         
#     def run(self):
#         print("Running chip-fel-flash")
#         commandRunner = CommandRunner(log)
#         errcode = commandRunner.call_and_return(cmd=["./chip-fel-flash.sh", "-f"], timeout=400 )
#         errcode = 0
#         print("Error code: " + str(errcode) )
#         if errcode != 0:
#             if not errcode in self.err_codes:
#                 errcode = -1
#             raise Exception( "Flashing failed: ", self.err_codes[ errcode ] )
# 
#     
#     
    
    
    