def json_response(status=200, msg=None, errors=None, data=None):
    #
    #   Common function for making json response
    #   response {
    #       status: StatusCode,
    #       msg: String
    #       errors: Object
    #   }
    #
    if data is None:
        data = {}
    if errors is None:
        errors = {}
    res = {"status": status}

    if msg is not None and type(msg) == str:
        res["msg"] = msg

    if len(errors.keys()):
        res["errors"] = errors

    for key in data:
        res[key] = data[key]

    return res, status
