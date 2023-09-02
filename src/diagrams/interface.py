"""
aggregates.py
"""
import logging
import os
import sys


def main():

    logger.info('Data structures for illustrations')


if __name__ == '__main__':

    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    path = os.path.join(root, 'warehouse', 'expenditure', 'diagrams')

    # Threads
    os.environ['NUMEXPR_MAX_THREADS'] = '8'

    # Logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    # Class
    import src.functions.directories

    directories = src.functions.directories.Directories()
    directories.cleanup(path=path)
    directories.create(path=path)


    main()
