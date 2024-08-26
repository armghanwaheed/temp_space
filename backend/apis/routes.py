from flask import Blueprint, jsonify
from .schema import CalculateMemorySchema
from .decorators import validate_request


api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/calculate_memory', methods=['POST'])
@validate_request(CalculateMemorySchema)
def calculate_model_memory(validated_data):
    """
    Handle model information request.
    """
    model_name = validated_data.get('model_name')
    token = validated_data.get('token')  # Token is optional
    response = {
        'model_name': model_name,
        'token': token
    }
    return jsonify(response), 200
