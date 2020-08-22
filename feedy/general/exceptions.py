class DataNotFoundException(Exception):
    pass


class IntegrityError(Exception):
    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)


class BusinessException(Exception):
    USERNAME_EXIST = 1
    PASSWORD_VALIDATION_ERROR = 2
    ENTITY_NOT_FOUND = 3
    FEED_ALREADY_EXIST = 4
    FEED_IS_INVALID = 5
    CHANNEL_ALREADY_FOLLOWED = 6

    def __init__(self, code, message=None, *args):
        super().__init__(*args)
        self.code = code
        self.message = message


class ConnectionException(Exception):
    def __init__(self, *args):
        super().__init__(*args)
