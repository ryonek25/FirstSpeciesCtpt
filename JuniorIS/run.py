from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .polyphony_model import PolyphonyRnnModel

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello Person!"


if __name__ == "__main__":
  app.run(debug=True)