from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler

from general.exceptions import BusinessException, DataNotFoundException, ConnectionException


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is None:
        if isinstance(exc, BusinessException):
            if exc.code == BusinessException.PASSWORD_VALIDATION_ERROR:
                return Response({"message": exc.message}, status=status.HTTP_409_CONFLICT)
            elif exc.code == BusinessException.USERNAME_EXIST:
                return Response({"message": "username exist"}, status=status.HTTP_409_CONFLICT)
            elif exc.code == BusinessException.FEED_ALREADY_EXIST:
                return Response({"message": "This channel already exist"}, status=status.HTTP_409_CONFLICT)
            elif exc.code == BusinessException.FEED_IS_INVALID:
                return Response({"message": "Channel address is invalid"}, status=status.HTTP_409_CONFLICT)
            elif exc.code == BusinessException.CHANNEL_ALREADY_FOLLOWED:
                return Response({"message": "You follow this channel already"}, status=status.HTTP_409_CONFLICT)
        elif isinstance(exc, DataNotFoundException):
            return Response({"message": "Entity not found"}, status=status.HTTP_404_NOT_FOUND)
        elif isinstance(exc, ConnectionException):
            return Response({"message": "Remote service not responding properly. Try later."},
                            status=status.HTTP_503_SERVICE_UNAVAILABLE)
    else:
        return response
