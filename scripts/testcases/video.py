#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from devicewrapper.android import device as d
import util as u

class VideoTest(unittest.TestCase):
    def setUp(self):
        super(VideoTest, self).setUp()
        d.wakeup()
        u.backHome(d)

    def tearDown(self):
        super(VideoTest, self).tearDown()
        u.backHome(d)

    def testVideoPlayer(self):
        #Find and launch Video app
        #assert d.exists(text='Video') , 'Video app not appear on the home screen'
        #d(text='Video').click.wait()
        d.start_activity(component='com.miui.video/.HomeActivity')
        assert d(text='我的视频').wait.exists(timeout=3000) , 'video app can not be launched.'

        d(text='我的视频').click.wait()
        assert d(text='bbb.mp4').wait.exists(timeout=3000) , 'Switch to local video.'
        d(text='bbb.mp4').click.wait()
        assert d(text='bbb.mp4').wait.gone(timeout=3000), 'Not switch to playing'

        d.sleep(600)
        assert d(text='bbb.mp4').wait.exists(timeout=10000)
        d.press('back')
        

