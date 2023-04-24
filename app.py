from flask import Flask
app=Flask(__name__)

# import controller.user_controller as user_controller
# import controller.product_controller as user_controller

from controller import *

@app.route('/')
def welcome():
    return "hello world"

@app.route('/home')
def home():
    return "This is the home page"