from service_api1.app import app, client


@app.route('/user', methods=['GET', 'POST', 'DELETE', 'PATCH'])
async def user(request):
    if request.method == 'GET':
        query = request.args
        data = client.db.users.find_one(query)
        return request.json(data), 200

    data = request.get_json()

    if request.method == "POST":
        if data.get('name', None) is not None and data.get('email', None) is not None:
            client.db.users.insert_one(data)
            return request.json({'ok': True, 'message': 'User created successfully!'}), 200
        else:
            return request.json({'ok': False, 'message': 'Bad request parameters!'}), 400

