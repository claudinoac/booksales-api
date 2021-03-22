from apps.book.repository import BookRepository


class BookValidator:
    command = None

    def __init__(self, command, session):
        self.command = command
        self.repository = BookRepository(session)

    def validate(self):
        errors = {}
        errors.update(self.validate_title_and_author())
        return errors

    def validate_title_and_author(self):
        book = self.repository.get_book_by_author_and_title(self.command.author, self.command.title)
        if book:
            return {"duplicated": "Book with title {} and author {} already exists.".format(
                self.command.title,
                self.command.author
            )}
        return {}
