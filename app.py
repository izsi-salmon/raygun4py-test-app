import os
import sys
from flask import Flask, current_app
from raygun4py.middleware import flask
from raygun4py import raygunprovider
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('RAYGUN_API_KEY')

client = raygunprovider.RaygunSender(api_key)

app = Flask(__name__)
flask.Provider(app, api_key, config={'filtered_keys': ['RAYGUN_API_KEY']}).attach()

def handle_exception(exc_type, exc_value, exc_traceback):
    sender = raygunprovider.RaygunSender(api_key)
    sender.send_exception(exc_info=(exc_type, exc_value, exc_traceback))

sys.excepthook = handle_exception

@app.route("/")
def hello():
  try:
      raise Exception("foo")
  except:
      client.send_exception()
  return "Hello world"

if __name__ == "__main__":
  app.run()