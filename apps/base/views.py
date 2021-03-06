import json

from marshmallow.exceptions import ValidationError
from tornado.web import HTTPError, RequestHandler
from tornado_sqlalchemy import SessionMixin

from apps.base.exceptions import CommandError, ViewError


class BaseView(RequestHandler):
    def write_error(self, status_code, **kwargs):
        self.finish({"error": {"status_code": status_code, "message": self._reason}})


class BaseModelView(BaseView, SessionMixin):
    serializer_class = None
    model = None

    def __init__(self, *args, **kwargs):
        if not self.serializer_class:
            raise ViewError("You have to define serializer_class attribute on {}".format(self.__class__.__name__))
        if not self.repository_class:
            raise ViewError("You have to define the repository_class attribute on {}".format(self.__class__.__name__))
        return super(BaseModelView, self).__init__(*args, **kwargs)


class BaseInstanceView(BaseModelView):
    def get(self, instance_id=None):
        if instance_id:
            repository = self.repository_class(self.session)
            instance = repository.get_by_id(instance_id)
            if not instance:
                raise HTTPError(404)
            serializer = self.serializer_class(instance)
            instance_data = serializer.as_dict()
        self.write(instance_data)


class BaseListView(BaseModelView):
    def get(self):
        repository = self.repository_class(self.session)
        instance_list = repository.get_all()
        if not instance_list:
            raise HTTPError(404)
        serializer = self.serializer_class(instance_list, multiple=True)
        instances_data = serializer.as_dict()
        self.write(instances_data)


class BaseModelCreateView(BaseView, SessionMixin):
    command_dispatcher = None
    handler_class = None

    def post(self):
        """Creates a new object in DB using command dispatcher and handler"""
        try:
            body_data = json.loads(self.request.body)
            command = self.command_dispatcher.Schema().load(body_data)
        except ValidationError as validation_error:
            self.set_status(400)
            self.write(validation_error.messages)
        except json.decoder.JSONDecodeError:
            self.set_status(400)
            self.write({"error": "Invalid body message"})
        else:
            handler = self.handler_class(self.session)
            try:
                command_output = handler.handle(command)
            except CommandError as command_error:
                self.set_status(400)
                command_output = command_error.message
            else:
                self.set_status(201)
            self.write(command_output)


class NotFoundView(BaseView):
    def get(self, *args, **kwargs):
        raise HTTPError(status_code=404, reason="Invalid resource path")
