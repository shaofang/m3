#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from devicewrapper.android import device as d
import util as u

class MessageTest(unittest.TestCase):
    def setUp(self):
        super(MessageTest, self).setUp()
        d.wakeup()
        #d.start_activity(action='android.intent.action.DIAL', data='tel:13581739891', flags=0x04000000)
        u.backHome(d)

    def tearDown(self):
        super(MessageTest, self).tearDown()
        u.backHome(d)

    def testMO_MTSms(self):
        str_receiver = '10086'
        str_content = 'Message Test Content'
        #assert d.exists(text='Messaging') , 'message app not appear on the home screen'
        #assert d.exists(text='Apps')  , 'apps not appear on the home screen'
        #d(text='Messaging').click.wait()

        d.start_activity(component='com.android.mms/.ui.MmsTabActivity')
        assert d(text='Messages').wait.exists(timeout=3000), 'can not launch message in 3s'

        if not d(text="No conversations.").wait.exists(timeout=1000):
            d(className='android.view.View').long_click()
            if d(text="Check All").wait.exists(timeout=3000):
                d(text="Check All").click.wait()
            d(text="Delete").click.wait()
            d(text="Delete").click.wait()

        d(text='New message').click.wait()
        d(className='android.widget.EditText', index=0).set_text(str_receiver)
        assert d(text=str_receiver).wait.exists(timeout=10000), 'receiver number input error'            
        d(className='android.widget.EditText', index=1).set_text(str_content)
        assert d(text=str_content).wait.exists(timeout=10000), 'content input error'            
        d(description='Send message').click.wait()
        assert d(text='Received').wait.exists(timeout=20000), 'sms sending failed in 20s'
        assert d(textStartsWith='尊敬的客户').wait.exists(timeout=20000), 'sms sending failed in 20s'

    def testMoMMS(self):
        str_receiver = '13501101339'
        str_content = 'Message Test Content'
        d.start_activity(component='com.android.mms/.ui.MmsTabActivity')
        assert d(text='Messages').wait.exists(timeout=3000), 'can not launch message in 3s'

        if not d(text="No conversations.").wait.exists(timeout=1000):
            d(className='android.view.View').long_click()
            if d(text="Check All").wait.exists(timeout=3000):
                d(text="Check All").click.wait()
            d(text="Delete").click.wait()
            d(text="Delete").click.wait()

        d(text='New message').click.wait()
        d(className='android.widget.EditText', index=0).set_text(str_receiver)
        assert d(text=str_receiver).wait.exists(timeout=10000), 'receiver number input error'            
        d(className='android.widget.EditText', index=1).set_text(str_content)
        assert d(text=str_content).wait.exists(timeout=10000), 'content input error' 

        d(description='Add attachments').click.wait()

        assert d(text='Capture picture').wait.exists(timeout=3000), 'no adding attachment panel' 
        d(text='Capture picture').click.wait()
        assert d(description='Shutter button').wait.exists(timeout=3000), 'no camera' 
        d(description='Shutter button').click.wait()
        d.sleep(1)
        d(className='android.widget.ImageView', index=1).click.wait()
        assert d(text='MMS').wait.exists(timeout=3000), 'add attachment failed'

        d(description='Send message').click.wait()

        assert d(text='Sending').wait.exists(timeout=5000), 'No sending status'
        d.sleep(20)
        assert d(text='Sending').wait.gone(timeout=20000), 'MMS sending failed in 40s'



            

