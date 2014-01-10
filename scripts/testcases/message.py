#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from devicewrapper.android import device as d
import util as u

class MessageTest(unittest.TestCase):
    def setUp(self):
        super(MessageTest, self).setUp()
        d.wakeup()
        u.backHome(d)

    def tearDown(self):
        super(MessageTest, self).tearDown()
        u.backHome(d)

    def testMO_MTSms(self):
        #Set receiver and msg content
        str_receiver = '10086'
        str_content = 'Message Test Content'

        #Start Messaging and check if sucessful
        d.start_activity(component='com.android.mms/.ui.MmsTabActivity')
        assert d(text='Messages').wait.exists(timeout=3000), 'can not launch message in 3s'

        #Delete messages if there is any message.
        if not d(text="No conversations.").wait.exists(timeout=2000):
            d(className='android.view.View').long_click()
            if d(text="Check All").wait.exists(timeout=3000):
                d(text="Check All").click.wait()
            d(text="Delete").click.wait()
            d(text="Delete").click.wait()
            assert d(text="No conversations.").wait.exists(timeout=3000), 'Delete messages failed'

        #Compose message
        d(text='New message').click.wait()
        d(className='android.widget.EditText', index=0).set_text(str_receiver)
        assert d(text=str_receiver).wait.exists(timeout=10000), 'receiver number input error'            
        d(className='android.widget.EditText', index=1).set_text(str_content)
        assert d(text=str_content).wait.exists(timeout=10000), 'content input error'            
        d(description='Send message').click.wait()
        assert d(text='Received').wait.exists(timeout=20000), 'sms sending failed in 20s'
        assert d(textStartsWith='尊敬的').wait.exists(timeout=30000), 'No feedback in 30s'

    def testMoMMS(self):
        #Set receiver and msg content
        str_receiver = '13501278511'
        str_content = 'Message Test Content'

        #Start Messaging and check if sucessful
        d.start_activity(component='com.android.mms/.ui.MmsTabActivity')
        assert d(text='Messages').wait.exists(timeout=5000), 'can not launch message in 5s'

        #Delete messages if there is any message.
        if not d(text="No conversations.").wait.exists(timeout=1000):
            d(className='android.view.View').long_click()
            if d(text="Check All").wait.exists(timeout=3000):
                d(text="Check All").click.wait()
            d(text="Delete").click.wait()
            d(text="Delete").click.wait()

        #Compose message
        d(text='New message').click.wait()
        d(className='android.widget.EditText', index=0).set_text(str_receiver)
        assert d(text=str_receiver).wait.exists(timeout=10000), 'receiver number input error'            
        d(className='android.widget.EditText', index=1).set_text(str_content)
        assert d(text=str_content).wait.exists(timeout=10000), 'content input error' 

        #Add attachment from camera
        d(description='Add attachments').click.wait()
        assert d(text='Capture picture').wait.exists(timeout=3000), 'no adding attachment panel' 
        d(text='Capture picture').click.wait()
        assert d(description='Shutter button').wait.exists(timeout=3000), 'no camera' 
        d(description='Shutter button').click.wait()
        u.sleep(1)
        d(className='android.widget.ImageView', index=1).click.wait()
        assert d(text='MMS').wait.exists(timeout=5000), 'add attachment failed'

        #Send MMS
        d(description='Send message').click.wait()
        assert d(text='Sending').wait.exists(timeout=5000), 'No sending status'
        u.sleep(20)
        assert d(text='Sending').wait.gone(timeout=70000), 'MMS sending failed in 90s'



            

