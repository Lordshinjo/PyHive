"""Trino integration tests.

These rely on having a Trino+Hadoop cluster set up.
They also require a tables created by make_test_tables.sh.
"""

from __future__ import absolute_import
from __future__ import unicode_literals

from pyhive import trino
from pyhive.tests.test_presto import TestPresto

_HOST = 'localhost'
_PORT = '8081'


class TestTrino(TestPresto):
    __test__ = True

    def connect(self):
        return trino.connect(host=_HOST, port=_PORT, source=self.id())