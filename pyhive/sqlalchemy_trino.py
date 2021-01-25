from pyhive import sqlalchemy_presto, trino


class TrinoDialect(sqlalchemy_presto.PrestoDialect):
    name = 'trino'

    @classmethod
    def dbapi(cls):
        return trino
