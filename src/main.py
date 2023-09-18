import logging
import os
import shutil
import sys
import pathlib


def __extraneous():

    for path in pathlib.Path.cwd().rglob('__pycache__'):
        if path.is_dir():
            try:
                shutil.rmtree(path)
            except PermissionError:
                raise Exception(f'Delete Permission Denied: {path}')
            else:
                logger.info(f'Deleted: {path}')


def main():
    logger.info('investments')

    # The Excel sheets cases
    messages = src.cases.interface.Interface().exc()
    logger.info(messages)

    # Ascertain comparable cost values by adjusting for inflation via a deflator
    messages = src.adjust.interface.Interface().exc()
    logger.info(messages)

    # Calculating metrics
    src.metrics.interface.Interface().exc()

    # Deleting __pycache__
    __extraneous()


if __name__ == '__main__':
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    # Threads
    os.environ['NUMEXPR_MAX_THREADS'] = '8'

    # logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    # classes
    import src.cases.interface
    import src.adjust.interface
    import src.metrics.interface

    main()
