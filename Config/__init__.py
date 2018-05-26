
import os
import shutil

class Config:

    def __init__(self):
        # Initialize all config values
        self.__vals = {}
        self.taskrc = os.path.expanduser('~/.taskrc')
        self.task_dir = os.path.expanduser('~/.task')
        self.ca   = None
        self.cert = None
        self.key  = None
        self.server = None
        self.port = None
        self.group = None
        self.user = None
        self.uuid = None


    def write_taskrc(self):
        # Make the task directory if it does not exist
        if not os.path.exists(self.task_dir):
            os.mkdir(self.task_dir)

        # create the ~/.taskrc file
        with open(self.taskrc, 'w') as fp:
            fp.write('data.location={}\n'.format(self.task_dir))
            fp.write('taskd.server={}:{}\n'.format(self.server, self.port))
            fp.write('taskd.key=~/.task/key.pem\n')
            fp.write('taskd.certificate=~/.task/cert.pem\n')
            fp.write('taskd.ca=~/.task/ca.pem\n')
            fp.write('taskd.credentials={}\/{}\/{}\n'.format(self.group, self.user, self.uuid))

        # copy key and certs into ~/.task
        shutil.copyfile(self.key, os.path.expanduser('~/.task/key.pem'))
        shutil.copyfile(self.cert, os.path.expanduser('~/.task/cert.pem'))
        shutil.copyfile(self.ca, os.path.expanduser('~/.task/ca.pem'))

    def use_taskrc(self, taskrc):
        pass
        
    #def __getattr__(self, name):
    #    print("__getattr__({})".format(name))
    #    if not name.startswith('_'):
    #        self.__vals[name]
#
    #def  __setattr__(self, name, val):
    #    print("__setattr__({}, {})".format(name, val))
    #    if not name.startswith('_'):
    #        self.__vals[name] = val
    #    #else:
    #    #    self.__dict__['__vals'][name] = val