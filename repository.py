import arguments
import datetime
import os


class Repository:
    def __init__(self, args):
        self.directory = args[arguments.DIRECTORY]
        self.temporary = args[arguments.TEMPORARY]
        self.tmp = os.path.join(self.temporary,
                                datetime.datetime.now()
                                .strftime('%Y%m%d%H%M%S'))

    def __str__(self):
        return f'''\
Directory: {self.directory}
         → {os.path.realpath(self.directory)}
Temporary: {self.tmp}
'''
