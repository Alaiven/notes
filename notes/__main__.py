from clint import arguments
from clint.textui import puts
from .dispatcher import dispatch


def main():
    args = arguments.Args()
    if not args:
        puts('No args given')
    else:
        dispatch(args.grouped)


if __name__ == '__main__':
    main()
