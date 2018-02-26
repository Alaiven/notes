from clint import resources
import json

_company_name = 'Alaiven'
_app_name = 'notes'
_file_name = 'config.txt'


class Config(object):

    def __init__(self):
        resources.init(_company_name, _app_name)
        self._name = _file_name

    def _deserialize(self):
        contents = resources.user.read(self._name)
        return json.loads(contents) if contents else {}

    def _serialize(self, val):
        contents = json.dumps(val)
        resources.user.write(self._name, contents)

    def store(self, key, value):
        val = self._deserialize()
        val[key] = value
        self._serialize(val)

    def get(self, key):
        val = self._deserialize()
        return val[key]
