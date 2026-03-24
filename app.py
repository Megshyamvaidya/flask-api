from flask import Flask,request
app=Flask(__name__)
users=[
    {'id':1,'name':"Megshyam",'email':'meg@gmail.com'},
    {'id':2,'name':'Om','email':'om@gmail.com'}
]

@app.route('/users',methods=['GET'])
def get_users():
    return {"Status":"Success",'data':users},200

@app.route('/users/<int:user_id>',methods=['GET'])
def get_user(user_id):
    for user in users:
        if user['id']==user_id:
            return {"Status":"Success",'data':user},200
    return {"error ":"User not found"},404

@app.route('/users',methods=['POST'])
def add_user():
    try:
        data=request.get_json()
        if not data or 'name' not in data:
            return {"Error":"Name is required"},400
        new_user={
            'id':len(users)+1,
            'name':data['name'],
            'email':data.get('email','')
        }
        users.append(new_user)
        return {"status":"success",'data':new_user},201
    except Exception as e:
        return {"error":"Internal server error"},500
@app.route('/users/<int:user_id>',methods=['PUT'])
def update_users(user_id):
    data=request.get_json()

    for user in users:
        if user['id']==user_id:
            if 'name'in data:
                user['name']=data['name']
            if 'email' in data:
                user['email']=data['email']
            
            return {'status':'updated','data':user},200
    return {'error':"user not found"},404
@app.route('/users/<int:user_id>',methods=['DELETE'])
def delete_users(user_id):
    for user in users:
        if user['id']==user_id:
            users.remove(user)
            return {"Status":"Deleted",'data':user},200

@app.route('/users/count',methods=['GET'])
def user_count():
    return {"total_users":len(users)},200

if __name__=='__main__':
    app.run(debug=True)