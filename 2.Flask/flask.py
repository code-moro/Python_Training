import re
import flask
import json
from flask import Flask,request,jsonify
from flask.helpers import make_response
from flask.wrappers import Request

app=Flask(__name__)

@app.route('/')
def index():
    return'<h2>Hello World</h2>'

@app.route('/user/<name>')
def user(name):
    return '<h2>hello ,%s!<h2>'  %name


@app.route('/headers')
def headers():
    user_agent=request.headers.get('User-Agent')
    return '<p>your browser is %s</p>' %user_agent


income=[{'des':"Product Based",'amount':500}]

@app.route('/incomes')
def get_income():
    return jsonify(income)

@app.route('/incomes',methods=["POST"])
def add_income():
    income.append(request.get_json())
    return 'Created',201


stock={
"fruits":{
    "apple":100,
    "cherry":70,
    "manago":80
}
}

@app.route('/stock')
def get_stock():
    res=make_response(jsonify(stock),200)
    return res


@app.route('/stock/<collection>/<member>')
def get_member(collection,member):
    if collection in stock:
        member=stock[collection].get(member)
        if member:
            res=make_response(jsonify(member),200)
            return res
        res=make_response(jsonify({"error":"Not found"}),404)
        return res
    res=make_response(jsonify({"error":"Not found"}),404)
    return res

@app.route("/stock/<collection>",methods=["PUT"])
def put_collection(collection):
    req=request.get_json()
    if collection in stock:
        stock[collection]=req
        res=make_response(jsonify({"msg":"collection updated"}),200)
        return res
    else:
        res=make_response(jsonify({"err":"not found"}),404)
        return res



@app.route("/stock/<collection>",methods=["DELETE"])
def delete_collection(collection):
    if collection in stock:
        del stock[collection]
        res=make_response(jsonify({"msg":"Deleted"}),204)
        return res
    else:
        res=make_response(jsonify({"error":"collection Not found"}),404)
        return res

@app.route("/stock/<collection>/<member>",methods=["DELETE"])
def member(collection,member):
    if collection in stock:
        if member in stock[collection]:
            del stock[collection][member]
            res=make_response(jsonify({"msg":"Deleted"}),204)
            return res
        else:
            res=make_response(jsonify({"error":"record Not found"}),404)
            return res  


if __name__=='__main__':
    print(income)
    app.run(debug=True)




"""
put method code for stocks
@app.route("/stock/<collection>", methods=["PUT"])
def put_collection(collection):
    req = request.get_json()
    if collection in stock:
        for key, value in req.items():
            if key in stock[collection]:
                stock[collection][key] = value

        res = make_response(jsonify({"msg": "Collection Updated"}), 200)
        return res
    stock[collection] = req
    res = make_response(jsonify({"msg": "Collection Created"}), 201)
    return res


"""