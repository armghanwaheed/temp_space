from functools import wraps

from flask import request, jsonify
from marshmallow import Schema, ValidationError


def validate_request(schema: Schema):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            schema_instance = schema()  # Instantiate the schema
            try:
                # Validate and deserialize input
                data = schema_instance.load(request.json)
            except ValidationError as err:
                return jsonify({'errors': err.messages}), 400

            # Pass the validated data as a keyword argument
            return f(*args, validated_data=data, **kwargs)
        return decorated_function
    return decorator
