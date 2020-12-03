import pytest
import requests
import json

url = 'http://127.0.0.1:5000' # The root url of the bank app

def test_index_page():              #test to get the index page
    r = requests.get(url + '/')
    assert r.status_code == 200

def test_get_all_users():               #test to fetch all users
    r = requests.get(url + '/Account')
    assert r.status_code == 200

    data = r.json()
    assert len(data) > 0

def test_non_existing_user():                 #test to check the non existing user
    r = requests.get(url + '/Account/srini')
    assert r.status_code == 404

def test_get_user():                #test to fetch the existing user
    r = requests.get(url + '/Account/jag')
    assert r.status_code == 200
    data = r.json()
    assert len(data) > 0
    assert data[0]['username']=='jag'

def test_post_user():                       #test to insert user details
    r = requests.post(url + '/Account', 
    json={"name": "aish","username" : "aish1", "password" : "a123",
    "address" : "sector","state" : "Chennai","country" : "India",
    "email" : "aish@gmail.com","pan" : "iiklogr90a",
    "contact" : "9878974536","DOB" : "13/03/1995",
    "accounttype": "current"})
    assert r.status_code == 200

def test_post_same_user():                       #test to insert same user details again
    r = requests.post(url + '/Account', 
    json={"name": "aish","username" : "aish1", "password" : "a123",
    "address" : "sector","state" : "Chennai","country" : "India",
    "email" : "aish@gmail.com","pan" : "iiklogr90a",
    "contact" : "9878974536","DOB" : "13/03/1995",
    "accounttype": "current"})
    assert r.status_code == 403
   
def test_update_user():                         #test to update user details
    r = requests.put(url + '/Account/aish1', 
    json={"name": "aishwarya","username" : "aish1", "password" : "a123",
    "address" : "sector","state" : "Chennai","country" : "India",
    "email" : "aish@gmail.com","pan" : "iiklogr90a",
    "contact" : "9878974536","DOB" : "13/03/1995",
    "accounttype": "current"})
    assert r.status_code == 200


def test_get_all_loans():               #test to fetch all loan data
    r = requests.get(url + '/Loan')
    assert r.status_code == 200

    data = r.json()
    assert len(data) > 0

def test_non_existing_loan():                 #test to check the non existing loan data
    r = requests.get(url + '/Loan/srini')
    assert r.status_code == 404

def test_get_loan():                #test to fetch the existing loan data
    r = requests.get(url + '/Loan/tar')
    assert r.status_code == 200
    data = r.json()
    assert len(data) > 0
    assert data[0]['username']=='tar'

def test_post_loan():                   #test to insert loan
    r = requests.post(url + '/Loan',
    json = { "loantype": "house", "loanamount": "5000000",
    "date": "20-07-1996", "rateofinterest": "9.5",
    "durationofloan": 20, "username": "aish1" })
    assert r.status_code == 200

def test_update_loan():                   #test to update loan 
    r = requests.put(url + '/Loan/aish1',
    json = { "loantype": "house", "loanamount": "5000000",
    "date": "20-07-1996", "rateofinterest": "9.5",
    "durationofloan": 30, "username": "aish1" })
    assert r.status_code == 200


def test_delete_loan_before():                     #test to delete loan data when user is present in database
    r = requests.delete(url + '/Loan/aish1')
    assert r.status_code == 200

def test_delete_user():                     #test to delete user data
   r = requests.delete(url + '/Account/aish1')
   assert r.status_code == 200

def test_delete_loan_after():                     #test to delete loan data after user is not exist
    r = requests.delete(url + '/Loan/aish1')
    assert r.status_code == 404

def test_getuser_after_deleteuser():                 #test to get user details after deleting user details
    r = requests.get(url + '/Account/aish1')
    assert r.status_code == 404

def test_updateuser_after_deleteuser():           #test to update user after deleting user details
    r = requests.put(url + '/Account/aish1', 
    json={"name": "aishwarya","username" : "aish1", "password" : "a123",
    "address" : "sector","state" : "Chennai","country" : "India",
    "email" : "aish@gmail.com","pan" : "iiklogr90a",
    "contact" : "9878974536","DOB" : "13/03/1995",
    "accounttype": "current"})
    assert r.status_code == 404