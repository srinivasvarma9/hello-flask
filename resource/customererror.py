from flask import jsonify
from flask import Response
errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     "AccountAlreadyExistsError": {
         "message": "Account with given name already exists",
         "status": 400
     }
}



class InternalServerError(Exception):
    pass

class AccountAlreadyExistsError(Exception):
    def to_json(self,message):
        return {"message": self.message}