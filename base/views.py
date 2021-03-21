from tornado.web import RequestHandler, HTTPError
from tornado_sqlalchemy import SessionMixin, as_future
from book.commands import CreateBookCommand
from marshmallow.exceptions import ValidationError

class BaseView(RequestHandler):
    def write_error(self, status_code, **kwargs):
        self.finish({
            'error': {
                'status_code': status_code,
                'message': self._reason
            }
        })


class BaseModelView(BaseView, SessionMixin):
    serializer_class = None
    model = None

    def __init__(self, *args, **kwargs):
        if not self.serializer_class:
            raise ViewError("You have to define serializer_class attribute on {}".format(
                self.__class__.__name__
                )
            )
        if not self.model:
            raise ViewError("You have to define the model attribute on {}".format(
                self.__class__.__name__
            ))
        return super(BaseModelView, self).__init__(*args, **kwargs)


class BaseInstanceView(BaseModelView):
    def get(self, instance_id=None):
        if instance_id:
            instance = self.session.query(self.model).filter_by(id=instance_id).first()
            if not instance:
                raise HTTPError(404)
            serializer = self.serializer_class(instance)
            instance_data = serializer.as_dict()
        self.write(instance_data)


class BaseListView(BaseModelView):
    def get(self):
        instance_list = self.session.query(self.model).all()
        serializer = self.serializer_class(instance_list, multiple=True)
        instances_data = serializer.as_dict()
        self.write(instances_data)




class NotFoundView(BaseView):
    def get(self, *args, **kwargs):
        raise HTTPError(
            status_code=404,
            reason="Invalid resource path"
        )
