from .note import Notes


_add_keys = ['-a', '-add', '--a', '--add']
_get_keys = ['-l', '-list', '--l', '--list']


def dispatch(arguments):
    add_key = list(_add_keys & arguments.keys())
    get_key = list(_get_keys & arguments.keys())

    if add_key:
        note = Notes()
        note.add(arguments[add_key[0]])
    elif get_key:
        note = Notes()
        note.get(arguments[get_key[0]])
