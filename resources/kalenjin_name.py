# Import Modules

from flask import request
from flask_restful import Resource
from http import HTTPStatus

# Import Model Classes from Models Package

from models.kalenjin_name import KalenjinName, kalenjin_name_list


# Define Resources
# Define KalenjinNameListResource

class KalenjinNameListResource(Resource):

    # Method to return all names

    def get(self):

        data = []

        for kalenjin_name in kalenjin_name_list:
            if kalenjin_name.is_publish is True:
                data.append(kalenjin_name.data)

            return {'data': data}, HTTPStatus.OK

    # Method to add new name

    def post(self):

        data = request.get_json()

        kalenjin_name = KalenjinName(boy_name=data['boy_name'],
                                     boy_name_trans=data['boy_name_trans'],
                                     girl_name=data['girl_name'],
                                     girl_name_trans=data['girl_name_trans'],
                                     girl_name_alternate=data['girl_name_alternate'],
                                     nickname=data['nickname'],
                                     english_meaning=data['english_meaning'],
                                     kalenjin_meaning=data['kalenjin_meaning'],
                                     related_name=data['related_name'],
                                     time_of_birth=data['time_of_birth'],
                                     event_at_birth=data['event_at_birth'],
                                     season_at_birth=data['season_at_birth'],
                                     pronunciation=data['pronunciation'],
                                     comment=data['comment'])

        kalenjin_name_list.append(kalenjin_name)

        return kalenjin_name.data, HTTPStatus.CREATED


# Define KalenjinNameResource

class KalenjinNameResource(Resource):

    # Method to return one name

    def get(self, kalenjin_name_id):
        kalenjin_name = next((kalenjin_name for kalenjin_name in kalenjin_name_list if
                              kalenjin_name.id == kalenjin_name_id and kalenjin_name.is_publish == True), None)

        if kalenjin_name is None:
            return {'message': 'Kalenjin name not found!'}, HTTPStatus.NOT_FOUND

        return kalenjin_name.data, HTTPStatus.OK

    # Method to update a name

    def put(self, kalenjin_name_id):
        data = request.get_json
