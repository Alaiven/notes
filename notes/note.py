from .config import Config
from .store import FirebaseStore


class Notes(object):

    def __init__(self):
        self.store = FirebaseStore('notes')

    def add(self, args):
        print(len(args))

    def get(self, args):
        vals = self.store.get_all()
        for v in vals:
            print(v)
