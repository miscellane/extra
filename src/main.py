import logging
import os
import sys


def main():
    logger.info('investments')

    years = range(1995, 2021)
    sample = src.cases.expenditure.Expenditure().exc(year=years[0])
    sample.info()
    logger.info(sample.head())


if __name__ == '__main__':
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    # logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    # classes
    import src.cases.expenditure

    main()
