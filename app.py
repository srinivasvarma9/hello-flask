import json
import requests
from flask import Flask, request, jsonify
from model.db import initilaize_db
from resource.accountsapi import account_api
from resource.loanapi import loan_api

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'accountsdb',
    'host': 'mongodb://localhost:27017/accountsdb',
    
}

initilaize_db(app)
account_api(app)
loan_api(app)

#url_request2="http://127.0.0.1:5050/"


@app.route('/', methods=['GET', 'POST'])
def basic():
    #respon = requests.get(url_request2+'/user')
    #print(respon.json())
    return "welcome user"

if __name__ == "__main__":
    app.run(debug=True)