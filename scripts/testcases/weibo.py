#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from devicewrapper.android import device as d
import util as u

class WeiboTest(unittest.TestCase):
    def setUp(self):
        super(WeiboTest, self).setUp()
        d.wakeup()
        u.backHome(d)

    def tearDown(self):
        super(WeiboTest, self).tearDown()
        u.backHome(d)

    def testWeibo_wifi(self):
        self.weibo(True)

    def testWeibo_3g(self):
        self.weibo(False)

    def weibo(self, wifi):
        u.openWifi(d, wifi)
        
        #Open sina weibo and check if successful
        d.start_activity(component='com.sina.weibo/.SplashActivity')
        assert d(className='android.widget.TextView', description="MainEdit").wait.exists(timeout=10000), 'weibo cient unable to open in 10 secs'

        #Clear the 'sent fail' prompt
        if d.exists(text='Sent failed. It has been saved in the draft.'):
            d(text='Sent failed. It has been saved in the draft.').click.wait()
            d.press('back')
        
        #Swipe to fetch new messages 3 times
        for i in range(5):
            #d.swipe(500, 500, 500, 1500, steps=15)
            d(description='首页列表').click.wait()
            d(className='android.widget.LinearLayout', index=0).click.wait()
            #assert d(textStartsWith='Refreshing').wait.exists(timeout=3000), 'No Refreshing...'
            #assert d(textStartsWith='Refreshing').wait.gone(timeout=60000), 'Refreshing fail in 60s'
            d.sleep(5)
        
        #Compose new message
        #Switch to message editor
        d(className='android.widget.TextView', description="MainEdit").click.wait()
        assert d(className='android.widget.TextView', text="New Weibo").wait.exists(timeout=3000), 'unable to compose message'
        
        #Fetch and input random TEXT, and send the message
        d(className='android.widget.EditText').set_text(u.fetchText())
        d(text='Send', description='Send').click.wait()
        assert not d(text='Sent failed. It has been saved in the draft.').wait.exists(timeout=10000), 'msg send failed'
        assert d(className='android.widget.TextView', description="MainEdit").wait.exists(timeout=10000), 'unable to back to home screen in 10 secs'
