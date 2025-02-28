from . import api
from ..models import User
from flask import request

@api.post('/signup')
def signUpAPI():
    data = request.json

    username = data['username']
    email = data['email']
    password = data['password']

    user = User.query.filter_by(username = username).first()
    if user:
        return {
            'status': 'not ok',
            'message': 'Please choose a different username.'
        }, 400
    user = User.query.filter_by(email = email).first()
    if user:
        return {
            'status': 'not ok',
            'message': 'That email is already in use.'
        }, 400

    user = User(username, email, password)
    user.saveToDB()
    return {
        'status': 'ok',
        'message': "You have successfully created an account."
    }, 201


