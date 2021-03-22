class BaseRepository:
    db_session = None
    model = None

    def __init__(self, db_session):
        self.db_session = db_session

    def get_by_id(self, object_id):
        return self.db_session.query(self.model).filter_by(id=object_id).first()

    def get_all(self):
        return self.db_session.query(self.model).all()

    def create_object(self, command):
        instance = self.model(**command.Schema().dump(command))
        self.db_session.add(instance)
        self.db_session.commit()
        return instance
