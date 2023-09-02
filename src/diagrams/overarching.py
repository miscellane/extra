"""
overarching.py
"""
import logging
import os
import sys

import pandas as pd


def main():
    """
    Entry point
    :return:
    """

    # The data set of top government divisions/segments
    data = src.functions.streams.Streams().read(
        uri=os.path.join(root, 'data', 'expenditure', 'expenditure_transaction_segments.csv'),
        usecols=['src', 'destination', 'segment_parent', 'segment_description', 'segment_code'])
    data.rename(columns={'segment_description': 'name',
                         'segment_parent': 'parent',
                         'segment_code': 'identifier'}, inplace=True)

    # For directed acyclic graph purposes, append a collapsed field.  If a node is collapsed, its
    # children are hidden by default
    data.loc[:, 'collapsed'] = None

    # The parent node's details
    node = pd.DataFrame(data={'src': None, 'destination': 'central', 'parent': None,
                              'name': 'Central Government Expenditure', 'identifier': '_T', 'collapsed': True},
                        index=[0])
    data = pd.concat([node, data], axis=0, ignore_index=True)

    # Save
    message = src.functions.objects.Objects().write(nodes=data.to_dict(orient='tight'),
                                                    path=os.path.join(path, 'overarching.json'))
    logger.info(message)


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
    import src.functions.streams
    import src.functions.objects
    import src.functions.directories

    directories = src.functions.directories.Directories()
    directories.cleanup(path)
    directories.create(path)

    main()
