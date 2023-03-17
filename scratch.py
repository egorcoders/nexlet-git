
import logging
logging.basicConfig(format='%(asctime)s | %(levelname)s: %(message)s', level=logging.NOTSET)
logging.debug('Here you have some information for debugging.')

def fn():
    return 2


logging.info(fn())

if __name__ == '__main__':
    fn()
