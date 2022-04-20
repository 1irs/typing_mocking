from dataclasses import dataclass
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.sql import text


@dataclass
class Repository:
    entity_id: str
    name: str
    bitbucket_id: str


def search_db(query: str) -> List[Repository]:
    eng = create_engine('postgresql://postgres:admin@localhost:5432/postgres')

    with eng.connect() as con:
        statement = text('SELECT * FROM public.repository WHERE name LIKE :q')
        statement = statement.bindparams(q='%'+query+'%')
        rs = con.execute(statement)

        res: List[Repository] = []
        for row in rs.fetchall():
            res.append(Repository(entity_id=row[0], name=row[1], bitbucket_id=row[2]))

        return res
