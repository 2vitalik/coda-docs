from coda.docs.adv19.mixins.indexer import IndexerMixin
from coda.lib import Coda


class ProjectThemes(IndexerMixin):
    def __init__(self, semester, coda_token):
        self.coda = Coda('adv18', semester, coda_token)
        self.table = self.coda.project_themes
        self.data = self.table.rows_dict()
        self.indexes = {}
        self.add_index('key')
        self.add_index('student')

    def by_key(self, key):
        return self.find('key', key)

    def by_student(self, student):
        return self.find('student', student)

    def update(self, row_id, changes):  # todo: move to common base class
        self.table.update(row_id, changes)
