from __future__ import absolute_import
from __future__ import unicode_literals

import contextlib

from sqlalchemy import create_engine

from pyhive.tests.test_sqlalchemy_presto import TestSqlAlchemyPresto


class TestSqlAlchemyTrino(TestSqlAlchemyPresto):
    def create_engine(self):
        return create_engine('trino://localhost:8081/hive/default?source={}'.format(self.id()))

    def test_bad_format(self):
        self.assertRaises(
            ValueError,
            lambda: create_engine('trino://localhost:8081/hive/default/what'),
        )

    def test_url_default(self):
        engine = create_engine('trino://localhost:8081/hive')
        try:
            with contextlib.closing(engine.connect()) as connection:
                self.assertEqual(connection.execute('SELECT 1 AS foobar FROM one_row').scalar(), 1)
        finally:
            engine.dispose()