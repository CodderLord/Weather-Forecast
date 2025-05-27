import json
import os
from functools import wraps

from flask import make_response, request

from Config import logger


def load_json_file(filename, default):
    try:
        if os.path.exists(filename):
            with open(filename, "r") as f:
                return json.load(f)
    except Exception as e:
        logger.error(f"Error loading {filename}: {str(e)}")
    return default


def save_json_file(filename, data):
    try:
        if not os.path.exists("DB"):
          os.makedirs("DB")
        with open(filename, "w") as f:
         json.dump(data, f, indent=2)
    except Exception as e:
        logger.error(f"Error saving {filename}: {str(e)}")


def get_user_id(req):
    # Get or create user ID from cookie
    user_id = req.cookies.get('user_id')
    if not user_id:
        import uuid
        user_id = str(uuid.uuid4())
    return user_id


def track_user_history(view_func):
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        response = make_response(view_func(*args, **kwargs))
        user_id = get_user_id(request)

        # Set user ID cookie if not present
        if not request.cookies.get('user_id'):
            response.set_cookie('user_id', user_id, max_age=365 * 24 * 60 * 60)

        return response

    return wrapper
