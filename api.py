from flask import Flask
import json
from flask import jsonify, request
import requests

app = Flask(__name__)
app.secret_key = "apimandi"

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

def getMandiData():
    r = requests.get('https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070?api-key=579b464db66ec23bdd000001783fbd26b2584e9346e3de7e60a31f35&format=json&offset=0&limit=10000')
    data = r.json()
    states = data['records']
    for i in states:
        if i['state'] == "NCT of Delhi":
          yield i
            

@app.route('/api/get')
def getData():
  i = getMandiData()
  emptyList = ['']
  for mandiData in i:
    emptyList.append(i)
  return jsonify(emptyList)


if __name__ == "__main__":
    app.run(debug=True)