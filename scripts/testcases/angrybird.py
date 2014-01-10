#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from devicewrapper.android import device as d
import util as u

class AngrybirdTest(unittest.TestCase):
    def setUp(self):
        super(AngrybirdTest, self).setUp()
        #d.start_activity(action='android.intent.action.DIAL', data='tel:13581739891', flags=0x04000000)
        d.wakeup()
        u.backHome(d)

    def tearDown(self):
        super(AngrybirdTest, self).tearDown()
        u.backHome(d)

    def testLaunch(self):
        #assert d.exists(text='Angry Birds') , 'wechat app not appear on the home screen'
        #assert d.exists(text='Apps')  , 'not appear on the home screen'
        #d(text='Angry Birds').click.wait()
        d.start_activity(component='com.rovio.angrybirdsstarwars.ads.iap/com.rovio.fusion.App')
        u.sleep(30)
        d.expect('loaded.png', timeout=10, msg='failed to load')
        d.press('back')
        d.expect('ok.png', timeout=10, msg='failed to find ok button')
        d.click(1060,590)