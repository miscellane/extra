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
        uri=os.path.join(root, 'data', 'expenditure_transaction_segments.csv'),
        usecols=['id', 'parent', 'segment_description', 'segment_code'])
    data.rename(columns={'segment_description': 'name', 'segment_code': 'identifier'}, inplace=True)

    # For directed acyclic graph purposes, append a collapsed field.  If a node is collapsed, its
    # children are hidden by default
    data.loc[:, 'collapsed'] = None

    # The parent node's details
    node = pd.DataFrame(data={'id': 'central', 'parent': None, 'name': 'Central Government',
                              'identifier': '_T', 'collapsed': True})
    data = pd.concat([node, data], axis=0, ignore_index=True)

    # Save
    message = src.functions.objects.Objects().write(nodes=data.to_dict(orient='tight'), path='')
    logger.info(message)


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

    import src.functions.streams
    import src.functions.objects

    main()