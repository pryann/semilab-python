def logger(message, logLevel='INFO', app='Semilab'):
    a = 'hi'
    print(f'{logLevel.upper()}: {message}, App: {app}')


logger('user login', 'ERROR', 'kutyimutyi')

logger(logLevel='DEBUG', message='test log')


def log_argv(*argv):
    print(argv)


log_argv(1)
log_argv(1, 2)
log_argv(1, 2, 3)


def log_kwargv(**kwargv):
    print(kwargv)


log_kwargv(first=1, second=2, third=3)


def log_argv_kwargv(*argv, **kwargv):
    print('Log', argv, kwargv)


log_argv_kwargv(1, 2, 3, first=1, second=2, third=3)
