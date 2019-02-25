import threading


def doubler(number):
    print(threading.current_thread().getName())
    print(number * 2)
    print('\n')


# if __name__ == '__main__':
#     for i in range(5):
#         t = threading.Thread(target=doubler, args=(i,))
#         t.start()

import logging

def get_logger():
    """
    Build logger used to save the state to local hardware
    :return:
    """
    logger = logging.getLogger("threading_example")
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler("threadind.log")
    fmt = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)

    logger.addHandler(fh)
    return logger


def doubler(num, logger):
    logger.debug('doubler function is executing...')
    res = num * 2
    logger.debug('doubler function get result: {}'.format(res))


# if __name__ == '__main__':
#     logger = get_logger()
#     thread_names = ['Mike', 'George', 'Wanda', 'Dingbat', 'Nina']
#     for i in range(5):
#         t = threading.Thread(target=doubler, args=(i, logger), name=thread_names[i])
#         t.start()

class MyThread(threading.Thread):
    def __init__(self, number, logger):
        threading.Thread.__init__(self)
        self.number = number
        self.logger = logger