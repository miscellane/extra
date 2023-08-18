import logging
import os
import sys


def main():
    logger.info('investments')

    messages = src.cases.interface.Interface().exc()
    logger.info(messages)

    src.algorithms.overall.Overall().exc()
    src.adjust.revalue.Revalue().exc()


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
    import src.algorithms.overall
    import src.adjust.revalue

    main()
