from datetime import datetime


def logger(func):
    def log(*args, **kargs):
        print('Processing Started ...')
        t1 = datetime.now()
        func(*args, **kargs)
        t2 = datetime.now()
        print('Processing Completed {} second(s)'.format(
            (t2 - t1).total_seconds()))

    return log
