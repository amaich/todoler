import time
import logging
from django.http import request
from django.http import response


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        
        self.get_response = get_response

        logging.basicConfig(level=logging.INFO, filename="todo_log.log")

    def __call__(self, req: request):
        resp = self.get_response(req)

        logging.info(f'===> Request: {req.method} {req.get_host()}{req.path}')
        logging.debug(f'Headers: {req.headers}')
        logging.info(f'Content params: {req.content_params}')
        logging.info(f'Body: {req.body}')
        logging.info(f'Status code: {resp.status_code}')

        return resp
