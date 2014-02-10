#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from devicewrapper.android import device as d
import util as u

class AngrybirdTest(unittest.TestCase):
    def setUp(self):
        super(AngrybirdTest, self).setUp()
        u.setup(d)

    def tearDown(self):
        super(AngrybirdTest, self).tearDown()
        u.teardown(d)

    def testLaunch(self):
        #Launch game
        d.start_activity(component='com.rovio.angrybirdsstarwars.ads.iap/com.rovio.fusion.App')
        u.sleep(30)
        d.expect('loaded.png', timeout=30, msg='failed to load')
        d.press('back')
        d.expect('ok.png', timeout=30, msg='failed to find ok button')
        d.click(1060,590)