from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from request import BatchRequestSchema
from data_converter import query_action

main_blueprint = Blueprint('main_blueprint', __name__)

file_name = 'data/apache_logs.txt'


@main_blueprint.route("/perform_query", methods=['POST'])
def perform_query():
    # получить параметры query и file_name, при ошибке вернуть ошибку 400
    data = request.json
    try:
        action_list = BatchRequestSchema().load(data)
    except ValidationError as e:
        return jsonify(e.messages), 400

    # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос

    result = None
    for query in action_list['queries']:
        result = query_action(
                cmd=query['cmd'],
                value=query['value'],
                file_name=file_name,
                data=result
        )
    # вернуть пользователю сформированный результат
    return jsonify(result)
