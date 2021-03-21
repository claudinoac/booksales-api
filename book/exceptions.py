

class BookValidationError(Exception):
    message = "Invalid book"

    def __init__(self, message):
        self.message = message
        return super(BookValidationError, self).__init__(message)

