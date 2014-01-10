#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from devicewrapper.android import device as d
import util as u

class MusicTest(unittest.TestCase):
    def setUp(self):
        super(MusicTest, self).setUp()
        d.wakeup()
        u.backHome(d)

    def tearDown(self):
        super(MusicTest, self).tearDown()
        u.backHome(d)

    def testMusicPlayer(self):
        #Launch Music and check if successful
        d.start_activity(component='com.miui.player/.ui.MusicBrowserActivity')
        assert d(text='4:35').wait.exists(timeout=5000) , 'Music app can not be launched in 3s.'

        d(text='4:35').click.wait()
        assert d(className='android.widget.SeekBar').wait.exists(timeout=5000) , 'Switch to music playing failed in 5s.'
        
        #Press 'next' button
        d(className='android.widget.LinearLayout', index=5).child(className='android.widget.ImageView', index=2).click.wait()

        #Stop
        d(className='android.widget.LinearLayout', index=5).child(className='android.widget.ImageView', index=1).click.wait()
        text1 = d(className='android.widget.LinearLayout', index=2).child(className='android.widget.TextView', index=0).text

        #Start
        d(className='android.widget.LinearLayout', index=5).child(className='android.widget.ImageView', index=1).click.wait()

        #Stop
        d(className='android.widget.LinearLayout', index=5).child(className='android.widget.ImageView', index=1).click.wait()
        text2 = d(className='android.widget.LinearLayout', index=2).child(className='android.widget.TextView', index=0).text

        assert text1!=text2, 'Not playing'
        
        d.press('back')
