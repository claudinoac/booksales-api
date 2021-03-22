class BaseModelCreateHandler:
    db_session = None
    serializer_class = None
    validator_class = None
    repository_class = None
    validation_exception = None

    def __init__(self, db_session):
        self.db_session = db_session

    def handle(self, command):
        validator = self.validator_class(command, self.db_session)
        errors = validator.validate()
        if not errors:
            repository = self.repository_class(self.db_session)
            created_object = repository.create_object(command)
            serializer = self.serializer_class(created_object)
            return serializer.as_dict()
        raise self.validation_exception(errors)
