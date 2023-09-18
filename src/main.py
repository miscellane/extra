"""main.py"""
import logging
import os
import sys


def main():
    logger.info('investments')

    # Data maps
    src.diagrams.interface.Interface().exc()

    # The Excel sheets cases
    messages = src.cases.interface.Interface().exc()
    logger.info(messages)

    # Ascertain comparable cost values by adjusting for inflation via a deflator
    messages = src.adjust.interface.Interface().exc()
    logger.info(messages)

    # Calculating metrics
    src.metrics.interface.Interface().exc()

    # Deleting __pycache__
    src.functions.extraneous.Extraneous().extraneous()


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
    import src.diagrams.interface
    import src.adjust.interface
    import src.metrics.interface
    import src.functions.directories
    import src.functions.extraneous

    src.functions.directories.Directories().cleanup(path=os.path.join(os.getcwd(), 'warehouse'))

    main()
