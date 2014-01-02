#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from devicewrapper.android import device as d
import time
import util as u

class BaiduTest(unittest.TestCase):
    def setUp(self):
        super(BaiduTest, self).setUp()
        d.wakeup()
        u.backHome(d)

    def tearDown(self):
        super(BaiduTest, self).tearDown()
        u.backHome(d)

    def testBaidumaps(self):
        #Check and set wifi
        u.openWifi(d, True)
        
        #assert d.exists(text='Browser') , 'Browser app not appear on the home screen'
        #assert d.exists(text='Apps')  , 'not appear on the home screen'
        #d(text='Browser').click.wait()
        
        #Launch browser
        d.start_activity(component='com.baidu.BaiduMap/com.baidu.baidumaps.WelcomeScreen')

        if d(text='不要福利').wait.exists(timeout=2000):
            d(text='不要福利').click.wait()

        assert d(text='附近').wait.exists(timeout=2000), 'No enter main map activity'
        assert d(text='路线').wait.exists(timeout=2000), 'No enter main map activity'

        d.swipe(510, 500, 510, 1000, steps=10)
        d.expect('location.png')
        d.click('location.png')
        d(text='我的位置').wait.exists(timeout=3000), 'can not locate'

