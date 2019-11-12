
import unittest2 as unittest
import shutil
import os
import re

import Config

class ConfigTestCase(unittest.TestCase):

    def setUp(self):
        shutil.rmtree('/tmp/test-task', ignore_errors=True,
            onerror=lambda funct, path, excinfo: path == '/tmp/test-task' and shutil.mkdir('/tmp/test-task'))

        for file in ('key.pem', 'ca.pem', 'cert.pem'):
            with open("/tmp/test-task/{}".format(file), 'w') as fp:
                fp.write("*** TLS Key file ***\n")

        print(os.system('ls -l /tmp/test-task'))


    def test_write_taskrc(self):
        """Validate that a .taskrc is created"""
        conf = Config.Config()
        conf.taskrc = '/tmp/.taskrc'
        conf.task_dir = '/tmp/.task'
        conf.key = '/tmp/test-task/key.pem'
        conf.cert = '/tmp/test-task/cert.pem'
        conf.ca = '/tmp/test-task/ca.pem'
        conf.server = 'test.freecinc.com'
        conf.port = 8383
        conf.group = 'Group4'
        conf.user = 'user101'
        conf.uuid = '000123-1234-5678-339204'
        conf.write_taskrc()

        self.assertTrue(os.path.exist('/tmp/.taskrc'))
        #self.assertTrue(os.path.exist('/tmp/.task/key.pem'))
        #self.assertTrue(os.path.exist('/tmp/.task/cert.pem'))
        #self.assertTrue(os.path.exist('/tmp/.task/ca.pem'))
