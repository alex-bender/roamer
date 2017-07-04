"""
argh
"""
import os
from roamer.entry import Entry
from roamer.record import Record
from roamer.constant import TRASH_DIR

COMMAND_ORDER = {'touch': 1, 'cp': 2, 'roamer-trash': 3}

class Command(object):
    def __init__(self, cmd, first_entry, second_entry=None):
        if cmd not in ('cp', 'roamer-trash', 'touch'):
            raise ValueError('Invalid command')
        if first_entry.__class__ != Entry:
            raise TypeError('first_entry not of type Entry')
        if second_entry.__class__ != Entry and second_entry != None:
            raise TypeError('second_entry not of type Entry or None')
        self.cmd = cmd
        self.first_entry = first_entry
        self.second_entry = second_entry
        # TODO: Modify switches based on whether entry is a directory
        # file name ends in / then is dir
        # """
        self.options = None


    def __str__(self):
        second_path = None
        if self.second_entry:
            second_path = self.second_entry.path
        parts = filter(None, (self.cmd, self.options, self.first_entry.path, second_path))
        return ' '.join(parts)

    def __lt__(self, other):
        return self.order_int() < other.order_int()

    def order_int(self):
        return COMMAND_ORDER[self.cmd]

    def execute(self):
        # TODO: Extract roamer-trash into a direct command
        if self.cmd == 'roamer-trash':
            self.cmd = 'mv'
            self.second_entry = Entry(self.first_entry.name, TRASH_DIR, self.first_entry.digest)
            Record.add_trash(self.first_entry.digest, self.second_entry.path)

        os.system(str(self))