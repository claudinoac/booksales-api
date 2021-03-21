class BaseRepository:
    db_session = None
    model = None

    def __init__(self, db_session):
        self.db_session = db_session

    def create_object(self, command):
        instance = self.model(**command.Schema().dump(command))
        self.db_session.add(instance)
        self.db_session.commit()
        return instance
