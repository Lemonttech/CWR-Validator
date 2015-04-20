# -*- encoding: utf-8 -*-

from pymongo import MongoClient

from cwr_validator.utils.mongo_encoder import MongoDictionaryEncoder
from cwr_validator.utils.repository import Repository


"""
Configuration to be used on the Mongo tests.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

host = '127.0.0.1'
port = 27017
db_name = 'commonworks'


class MongoGenericRepository(Repository):
    """
    Repository prepared to work with Mongo DB.
    """
    ELEMENTS_PER_PAGE = 15

    def __init__(self, repo_host, repo_port, repo_db_name, collection):
        connection = MongoClient(repo_host, repo_port)
        self._db = connection[repo_db_name]

        self._encoder = MongoDictionaryEncoder()

        self._collection = collection

    def add(self, entity):
        encoded = self.encoder.encode(entity)
        self._db[self._collection].insert(encoded)

    def get(self, predicate):
        # In Python 3 filter() returns an iterator
        # To avoid problems the result is set into a list
        return list(filter(predicate, self.__entities()))

    def remove(self, entity):
        self._db[self._collection].remove(self.encoder.encode(entity))

    def update(self, entity):
        self._db[self._collection].insert(self.encoder.encode(entity))

    def clear(self):
        self._db[self._collection].drop()

    @property
    def collection(self):
        return self._collection

    @property
    def encoder(self):
        return self._encoder

    def __entities(self):
        return list(self._db[self.collection].find())

    def __entities_by_page(self, page_number):
        return list(self._db[self.collection].find().skip(int(page_number) * self.ELEMENTS_PER_PAGE).limit(
            self.ELEMENTS_PER_PAGE))