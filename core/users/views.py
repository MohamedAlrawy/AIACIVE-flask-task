import json
from flask import jsonify, request, Response
from models import User
from core import models
from .serializers import UserSerializer
from . import users


"""
API accepting get and post methods.
For listing all users and adding new user.

post body = {
    'name': 'string',
    'email': 'email@email' # Must be unique.
}
"""
@users.route('/', methods=['GET', 'POST'])
def users_list():
    if request.method == 'GET':
        users = User.query.all()
        return jsonify(UserSerializer(many=True).dump(users))
    
    # post method (Add user)
    else:
        try:
            user = User(
                name=request.json.get('name', ''),
                email=request.json.get('email', '')
            )
            models.session.add(user)
            models.session.commit()
            return Response(json.dumps(UserSerializer().dump(user)), status=201, mimetype='application/json')
        except:
            return Response(json.dumps({'error': 'There was an issue adding user'}),
                            status=400, mimetype='application/json')

"""
API accepting get, update and delete methods.
For retrieve specific user, updating or deleting him.

put request body = {
    'name': 'string',
    'email': 'email@email' # Must be unique.
}
"""
@users.route('/<int:id>/', methods=['GET', 'DELETE', 'PUT'])
def user_detail(id):
    
    # handle get request
    if request.method == 'GET':
        user = User.query.get_or_404(id)
        return jsonify(UserSerializer().dump(user))
    
    # handle put request
    elif request.method == 'PUT':
        try:
            user = User.query.get_or_404(id)
            name = request.json.get('name', None)
            email = request.json.get('email', None)

            if name:
                user.name = name
            
            if email:
                user.email = email

            models.session.commit()

            return Response(json.dumps(UserSerializer().dump(user)), status=200, mimetype='application/json')
        except:
            return Response(json.dumps({'error': 'There was an issue updating user'}),
                            status=400, mimetype='application/json')
    
    # handle delete request
    else:
        user = User.query.get_or_404(id)
        try:
            models.session.delete(user)
            models.session.commit()
            return Response(json.dumps({}), status=204, mimetype='application/json')
        except:
            return Response(json.dumps({'error': 'There was an issue deleting user'}),
                            status=400, mimetype='application/json')
