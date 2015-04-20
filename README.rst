CWR Data Model Validator
========================

Validator service for CWR files. It receives a file following the CISAC CWR
standard v2.1 and returns a JSON containing the data from that same file.

It uses the `CWR Data Model`_ API, and it is recommended using that same library
to read the JSON created by the service.

Documentation
-------------

The current version is under development. No public documentation is still offered.

Status
------

The project is still in the development phase.

Issues management
~~~~~~~~~~~~~~~~~

Issues are managed at the GitHub `project issues page`_.

Building the code
-----------------

The application has been coded in Python, without using any particular framework.

Prerequisites
~~~~~~~~~~~~~

The project has been tested in the following versions of the interpreter:

- Python 2.6
- Python 2.7
- Pypy

Al other dependencies are indicated on requirements.txt, which can be installed with the command:

``pip install -r requirements.txt``

Getting the code
~~~~~~~~~~~~~~~~

The code can be found at the `GitHub project page`_.

License
-------

The project has been released under the `MIT License`_.

.. _CWR Data Model: https://github.com/weso/CWR-DataApi
.. _project issues page: https://github.com/weso/CWR-Validator/issues
.. _GitHub project page: https://github.com/weso/CWR-Validator
.. _MIT License: http://www.opensource.org/licenses/mit-license.php