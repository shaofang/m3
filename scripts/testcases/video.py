#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from devicewrapper.android import device as d
import util as u

class VideoTest(unittest.TestCase):
    def setUp(self):
        super(VideoTest, self).setUp()
        u.setup(d)

    def tearDown(self):
        super(VideoTest, self).tearDown()
        u.teardown(d)

    def testVideoPlayer(self):
        #Start video player and check if successful
        d.start_activity(component='com.miui.video/.HomeActivity')
        assert d(text='Local').wait.exists(timeout=5000) , 'video app can not be launched.'

        #Go to local video and start to play video
        d(text='Local').click.wait()
        assert d(text='bbb.mp4').wait.exists(timeout=3000) , 'Switch to local video.'
        d(text='bbb.mp4').click.wait()
        assert d(text='bbb.mp4').wait.gone(timeout=3000), 'Not switch to playing'

        #Wait to finish playing and check if back to video list
        u.sleep(600)
        assert d(text='bbb.mp4').wait.exists(timeout=10000)