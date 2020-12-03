from model.accounts import Accounts
import json
import requests
from flask import Flask, request, jsonify
#from resource.customerror import AccountAlreadyExistsError,to_json
#from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError

def account_api(app):
    @app.route('/Account',methods=['POST'])
    def create_account():
        #try:
            record = json.loads(request.data)
            x=Accounts.objects(username=record['username'])
            y=x.count()
            if y>0:
                return jsonify({"output":"Username already exists.please provide another!!"}),403
               # raise AccountAlreadyExistsError("user already exists bro")
            else:
                customer = Accounts(name=record['name'],username=record['username'],password=record['password'],address=record['address'],state=record['state'],country=record['country'],email=record['email'],pan=record['pan'],contact=record['contact'],DOB=record['DOB'],accounttype=record['accounttype'])
                return jsonify(customer.save())
        #except AccountAlreadyExistsError as e:
            #print(e)
            #return e.to_json()



    @app.route('/Account',methods=['GET'])
    def get_accounts():
        return jsonify(Accounts.objects())

    @app.route('/Account/<customer_id>',methods=['PUT'])
    def update_account(customer_id):
        x=Accounts.objects(username=customer_id)
        y=x.count()
        if y>0:
            record = json.loads(request.data)
            customer = Accounts.objects(username=customer_id)
            customer.update(name=record['name'],username=record['username'],password=record['password'],address=record['address'],state=record['state'],country=record['country'],email=record['email'],pan=record['pan'],contact=record['contact'],DOB=record['DOB'],accounttype=record['accounttype'])
            return jsonify(customer)
        else:
            #customer not found
            return "user does not exists",404
    @app.route('/Account/<customer_id>',methods=['DELETE'])
    def delete_account(customer_id):
        x=Accounts.objects(username=customer_id)
        y=x.count()
        if y>0:
            #delete the details in mongodb
            customer = Accounts.objects(username=customer_id)
            customer.delete()
            return jsonify(customer)
        else:
            #customer not found
            return "user does not exists",404 

    @app.route('/Account/<customer_id>',methods=['GET'])
    def get_account(customer_id):
        # record = json.loads(request.data)
        x=Accounts.objects(username=customer_id)
        y=x.count()
        if y>0:
            #get the updated details of single resource
            return jsonify(Accounts.objects(username=customer_id))
        else:
            #customer not found
            return "user does not exists",404