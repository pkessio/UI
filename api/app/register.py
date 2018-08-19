from flask import Flask, request, flash, redirect, url_for, jsonify
from functools import wraps

def check_auth(email, password):
    return email == 'admin' and password == 'secret'

def authenticate():
    message = {'message': "Authenticate."}
    resp = jsonify(message)

    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="login"'

    return resp