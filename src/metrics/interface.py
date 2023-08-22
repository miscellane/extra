"""
interface.py
"""
import os
import logging

import src.metrics.overall
import src.functions.objects


class Interface:
    """

    """

    def __init__(self):
        """

        """

        self.__storage = ''

        # logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def __persist(self, dictionary) -> str:
        """

        :param dictionary:
        :return:
        """

        return src.functions.objects.Objects().write(
            nodes=dictionary, path=os.path.join(self.__storage, 'overall.json'))

    def exc(self):

        overall = src.metrics.overall.Overall().exc()
        self.__logger.info(overall)

        parts = []
        for interest in ['annual_total', 'annual_segment_%', 'series_delta_%']:

            frame = overall[['epoch', interest, 'segment_code']]
            structure = frame.pivot(index='epoch', columns='segment_code', values=interest)
            structure.reset_index(drop=False, inplace=True)
            node = structure.to_dict(orient='tight')
            node['name'] = interest
            parts.append(node)

        self.__logger.info(parts)
