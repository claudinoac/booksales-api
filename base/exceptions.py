

class CommandError(Exception):
    message = {"error": "Invalid Command."}

    def __init__(self, message):
        self.message = message
        super(CommandError, self).__init__(message)
