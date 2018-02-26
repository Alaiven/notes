from google.cloud import firestore
from .config import Config

_firebase_cred_link = 'firebase_cred_link'


class FirebaseStore(object):

    def __init__(self, prefix):
        config = Config()
        self.prefix = prefix
        self.db = firestore.Client.from_service_account_json(
            config.get(_firebase_cred_link)
        )

    @staticmethod
    def _to_result(res):
        return list(map(lambda i: i.to_dict(), res))

    def get_all(self):
        return self._to_result(
            self.db.collection('notes').get())

    def get(self, id):
        return None
