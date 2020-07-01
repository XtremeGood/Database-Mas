from . import interface
from psqlextra.query import ConflictAction

class Dematad(interface.Interface):

    def update_database(self):
        for chunk in self.get_data(self.file_obj):
            chunk_as_dict = [dict(zip(self.all_cols, i))
                             for i in chunk]
            self.inserts += len(chunk)
            self.model.objects.on_conflict(
                ['DPID', 'CLID'],  ConflictAction.UPDATE
            ).bulk_insert(
                chunk_as_dict
            )
