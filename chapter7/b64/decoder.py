import base64


def base64_to_str(b64_data):

    return base64.b64decode(b64_data).decode('utf-8')