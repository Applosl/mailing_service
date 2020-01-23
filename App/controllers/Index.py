# coding=utf-8

from flask_restful import Resource, reqparse
from App.components import ControllerBase

from App.middleware import Mailer


class Index(Resource):
    @ControllerBase.request_auth()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('sender', required=True, type=str, help='error sender', location='json')
        parser.add_argument('title', required=True, type=str, help='error title', location='json')
        parser.add_argument('content', required=True, type=str, help='error content', location='json')
        args = parser.parse_args()

        receivers = [args['sender']]
        subject = args['title']
        message = args['content']
        Mailer.send_mail(receivers, subject, message)
        return ControllerBase.return_success()
