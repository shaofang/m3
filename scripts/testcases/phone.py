#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
import time
from devicewrapper.android import device as d
import util as u

class PhoneTest(unittest.TestCase):
    def setUp(self):
        super(PhoneTest, self).setUp()
        u.setup(d)

    def tearDown(self):
        super(PhoneTest, self).tearDown()
        if d(className='android.widget.Button', index=1):
            d(className='android.widget.Button', index=1).click.wait()
        u.teardown(d)

    def testMoCall(self):
        #Start dialer and confirm if dialer is launched
        d.start_activity(component='com.android.contacts/.activities.TwelveKeyDialer')
        assert d(text='Keypad').wait.exists(timeout=3000), 'Launch dialer failed'
        
        #MO call to 10086(cmcc) or 10010(unicom)
        d(description='one').click()
        d(description='zero').click()
        d(description='zero').click()
        d(description='eight').click()
        d(description='six').click()
        assert d.exists(text="10086") , 'Input number error!'
        
        #Press the call button
        d(text='Keypad').click.wait()
        
        #Wait 'Dialing' to see if begin to dial, and wait 'Dialing' disappear to see if connected. 
        #Wait '0:10' to see if duration is over 10s.  
        assert d(text="Dialing").wait.exists(timeout=10000), 'Should begin to dialing in 10 secs'
        assert d(text="Dialing").wait.gone(timeout=10000), 'Should connect in 10 secs'
        assert d(textStartsWith="0:1").wait.exists(timeout=15000), 'Call duration should be 10 secs'

        d(className='android.widget.Button', index=1).click.wait()
        assert d(text='Keypad').wait.exists(timeout=5000), 'Should back to dialer in 5s.'


