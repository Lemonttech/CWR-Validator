# -*- encoding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import os
import codecs

from werkzeug.utils import secure_filename
from cwr.parser.decoder.file import default_file_decoder
from cwr.parser.encoder.cwrjson import JSONEncoder


__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class FileService(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_files(self):
        raise NotImplementedError('The get_files method must be implemented')

    @abstractmethod
    def get_file(self, id):
        raise NotImplementedError('The get_data method must be implemented')

    @abstractmethod
    def save_file(self, file, path):
        raise NotImplementedError('The save_file method must be implemented')

    @abstractmethod
    def generate_json(self, data):
        raise NotImplementedError('The generate_json method must be implemented')


class LocalFileService(FileService):
    def __init__(self, path):
        super(FileService, self).__init__()
        self._files_data = {}
        self._path = path
        self._decoder = default_file_decoder()
        self._encoder_json = JSONEncoder()

    def get_file(self, file_id):
        file_id = int(file_id)

        if file_id in self._files_data:
            data = self._files_data[file_id]
        else:
            data = None

        return data

    def get_files(self):
        files = []

        for value in self._files_data.itervalues():
            files.append(value)

        return files

    def save_file(self, file, path):
        filename = secure_filename(file.filename)
        file.save(os.path.join(path, filename))

        data = self._read_cwr(filename, self._path)
        if data:
            index = len(self._files_data)
            self._files_data[index] = data
        else:
            index = None

        return index

    def _read_cwr(self, filename, path):
        file_path = os.path.join(path, filename)
        data = {}

        data['filename'] = filename
        data['contents'] = codecs.open(file_path, 'r', 'latin-1').read()

        try:
            result = self._decoder.decode(data)
        except:
            result = None

        return result

    def generate_json(self, data):
        return self._encoder_json.encode(data)
