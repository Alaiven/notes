from .post import Posts
from .category import Categories
from .user import Users
from .options import Options
from clint.textui import puts

_type_keys = ['p', 'post', 'u', 'user', 'c', 'category', 'o', 'options']

_add_keys = ['-a', '-add', '--a', '--add']
_get_keys = ['-l', '-list', '--l', '--list']
_del_keys = ['-d', '-delete', '--d', '--delete']

_dispatch_dict = {
    'p': lambda: Posts(),
    'u': lambda: Users(),
    'c': lambda: Categories(),
    'o': lambda: Options()
}


def dispatch(arguments):
    type_arg = arguments['_'][0]

    if type_arg in _type_keys:
        type_letter = type_arg[0]
        _dispatch_action(_dispatch_dict[type_letter], arguments)
    else:
        puts('Object type not provided or invalid')


def _dispatch_action(new_object, args):
    add_key = list(_add_keys & args.keys())
    get_key = list(_get_keys & args.keys())
    del_key = list(_del_keys & args.keys())

    obj = new_object()

    if add_key:
        obj.add(args[add_key[0]])
    elif get_key:
        obj.get(args[get_key[0]])
    elif del_key:
        obj.delete(args[del_key[0]])
    else:
        puts('Unknown action. Possible actions: -add, -list, -delete')
