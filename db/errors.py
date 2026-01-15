class DatabaseError(Exception):
    pass


class TableExistsError(DatabaseError):
    pass


class TableNotFoundError(DatabaseError):
    pass


class ConstraintError(DatabaseError):
    pass
