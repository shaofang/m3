#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from devicewrapper.android import device as d
import util as u

class CameraTest(unittest.TestCase):
    def setUp(self):
        super(CameraTest, self).setUp()
        d.wakeup()
        #d.start_activity(action='android.intent.action.DIAL', data='tel:13581739891', flags=0x04000000)
        u.backHome(d)

    def tearDown(self):
        super(CameraTest, self).tearDown()
        u.backHome(d)

    def testTakePicture(self):
        #assert d.exists(text='Camera') , 'camera app not appear on home screen'
        #assert d.exists(text='Apps')
        #d(text='Camera').click.wait()
        d.start_activity(component='com.android.camera/.Camera')
        assert d(description='Shutter button').wait.exists(timeout=3000), 'can not launch camera in 3s'

        d(description='Shutter button').click.wait()
        d.sleep(1)
        d(description='Most recent photo').click.wait()
        assert d(text="Delete").wait.exists(timeout=3000), 'No picture to delete.'
        d(text="Delete").click.wait()
        d(text="OK").click.wait()
        #If there is not only one picture
        if d(text="Delete").wait.exists(timeout=2000):
            d.press('back')
        assert d(description="Shutter button").wait.exists(timeout=3000), 'unable back to camera after delete.'

        
            


