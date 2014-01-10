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

        #Launch Baidu map app
        d.start_activity(component='com.baidu.BaiduMap/com.baidu.baidumaps.WelcomeScreen')

        if d(text='不要福利').wait.exists(timeout=3000):
            d(text='不要福利').click.wait()

        #Check if baidu map can be launched successfully
        assert d(text='附近').wait.exists(timeout=2000), 'No enter main map activity'
        assert d(text='路线').wait.exists(timeout=2000), 'No enter main map activity'

        #Swipe on the map
        d.swipe(510, 500, 510, 1000, steps=10)

        #Locate to current location
        d.expect('location.png')
        d.click('location.png')

        #Located successful
        assert d(text='我的位置').wait.exists(timeout=3000), 'can not locate'

