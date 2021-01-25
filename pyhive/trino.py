from pyhive import presto


def connect(*args, **kwargs):
    """Constructor for creating a connection to the database. See class :py:class:`Connection` for
    arguments.

    :returns: a :py:class:`Connection` object.
    """
    return Connection(*args, **kwargs)


class Connection(presto.Connection):
    def cursor(self):
        return Cursor(*self._args, **self._kwargs)


class Cursor(presto.Cursor):
    header_prefix = 'X-Trino'
