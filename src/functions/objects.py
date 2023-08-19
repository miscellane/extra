"""
objects.py
"""
import requests
import json
import pathlib


class Objects:
    """

    """

    def __init__(self):
        """

        """

    @staticmethod
    def write(nodes: any, path: str) -> str:
        """

        :param nodes:
        :param path:
        :return:
        """

        name = pathlib.Path(path).stem

        if not bool(nodes):
            return f'{name}: empty'

        try:
            with open(file=path, mode='w', encoding='utf-8') as disk:
                json.dump(obj=nodes, fp=disk, ensure_ascii=False, indent=4)
            return f'{name}: succeeded'
        except IOError as err:
            raise Exception(err) from err

    @staticmethod
    def api(url: str) -> dict:
        """

        :param url:
        :return:
        """

        try:
            response = requests.get(url=url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise Exception(f'HTTP Error: {err}')
        except Exception as err:
            raise Exception(err) from err

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Failure code: {response.status_code}')

    @staticmethod
    def read(uri: str) -> dict:
        """

        :param uri:
        :return:
        """

        try:
            with open(file=uri, mode='r') as disk:
                return json.load(fp=disk)
        except ImportError as err:
            raise Exception(err) from err
