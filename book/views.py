from base.views import BaseInstanceView, BaseListView
from book.models import Book
from book.serializers import BookSerializer
from marshmallow.exceptions import ValidationError
from book.commands import CreateBookCommand
from tornado.web import HTTPError
from book.handlers import CreateBookHandler
from book.validators import BookValidationError
import json


class BookInstanceView(BaseInstanceView):
    serializer_class = BookSerializer
    model = Book


class BookListView(BaseListView):
    serializer_class = BookSerializer
    post_command = CreateBookCommand
    model = Book

    def post(self):
        try:
            body_data = json.loads(self.request.body)
            command = CreateBookCommand.Schema().load(body_data)
        except ValidationError as validation_error:
            self.set_status(400)
            self.write(validation_error.messages)
        except json.decoder.JSONDecodeError:
            self.set_status(400)
            self.write({"error": "Invalid body message"})
        else:
            handler = CreateBookHandler(self.session)
            try:
                result = handler.handle(command)
            except BookValidationError as validation_error:
                self.set_status(400)
                command_output = validation_error.message
            else:
                self.set_status(201)
                command_output = command.Schema().dump(command)
                command_output["price"] = str(command_output["price"])
            self.write(command_output)
