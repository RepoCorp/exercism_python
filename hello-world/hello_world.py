#
# Skeleton file for the Python "Hello World" exercise.
#


def hello(name=''):
    if name == '':
        return 'Hello, World!'
    else:
        return u'Hello, {0}!'.format(name)
