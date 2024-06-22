import duckdb


def getNumber() -> int:
    return duckdb.sql("SELECT 42").fetchall()[0][0]
