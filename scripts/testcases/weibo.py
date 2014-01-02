#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from devicewrapper.android import device as d
import util as u
import random

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
        #assert d.exists(text='Weibo') , 'wechat app not appear on the home screen'
        #assert d.exists(text='Apps')  , 'not appear on the home screen'
        #d(text='Weibo').click.wait()
        account = 'funnyborqs'
        d.start_activity(component='com.sina.weibo/.SplashActivity')
        assert d(description='MainEdit').wait.exists(timeout=10000), 'weibo client unable to open in 10 secs'

        #if d.exists(text='Sent failed. It has been saved in the draft.'):
        #    d(text='Sent failed. It has been saved in the draft.').click.wait()
        #    d.press('back')
        d.swipe(500, 500, 500, 1000)
        d.sleep(5)
        
        d(description='MainEdit').click.wait()
        assert d(className='android.widget.TextView', text="New Weibo").wait.exists(timeout=3000), 'unable to compose message'
        
        n=random.randint(15, 30)
        
        d(className='android.widget.EditText').set_text(''.join(self.content(n)))
        d(className='android.widget.TextView', text='Send').click.wait()
        assert not d(text='Sent failed. It has been saved in the draft.').wait.exists(timeout=15000), 'msg send failed'
        #assert d(className='android.widget.TextView', description="MainEdit").wait.exists(timeout=10000), 'unable to back to home screen in 10 secs'

    def content(self, n):
        s = ' !.,abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        return ''.join(random.sample(s, n))
        

