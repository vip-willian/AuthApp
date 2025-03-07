from flask_restful import Resource


class UserLogin(Resource):
    def post(self):
        pass


class UserLogout(Resource):
    def post(self):
        pass


class GetUserList(Resource):
    def get(self):
        pass

class GetUserById(Resource):
    def get(self, id):
        return {'userId': id}
