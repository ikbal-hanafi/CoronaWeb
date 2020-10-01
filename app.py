from flask import Flask, render_template, url_for
from modules import modules
import shutil

try: shutil.rmtree("modules/__pycache__")
except Exception as r: print(r)

app = Flask(__name__)
covid = modules.Covid()

@app.route("/global/<country>")
def world(country):
  covid.get()
  data = covid.all
  status = covid.search(country=country)
  return render_template("global.html", status=status, country=country, values=zip(range(len(data)), data),)

@app.route("/")
def index():
  covid.get()
  data = covid.all
  local = covid.search(country="indo")
  return render_template("index.html", values=zip(range(len(data)), data), local=local)
  
if __name__ == "__main__":
  app.run(debug=True, port=8080)