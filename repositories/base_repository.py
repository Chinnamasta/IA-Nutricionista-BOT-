from tinydb import table
from projeto.database.engine import Engine

class BaseRepository(Engine):
    def get_table(self, table_name: str) -> table.Table:
        return self.db.table(table_name)
        
