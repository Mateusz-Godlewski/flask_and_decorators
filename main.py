# from flask import Flask
#
#
# app = Flask(__name__)
#
# @app.route("/")
# def hello_world():
#     return "Hello World!"
#
# if __name__ == "__main__":
#     app.run()



def decorator_world(function):
    def wrapper_function():
        function()
        print("World!")
    return wrapper_function


@decorator_world
def hello():
    print("Hello")


hello()