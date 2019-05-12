from flask import Flask
import DigiAssistant_Server as Agent

app = Flask(__name__)

@app.route("/<string:requestText>")
def translate(requestText):
    #responseText=requestText+"----test----"
    responseText = Agent.detect_intent_texts('df-eva-agent',1,requestText,'en')
    return responseText

if __name__ == '__main__':
    app.run(host='0.0.0.0') #app.run(debug=True), app.run(host='0.0.0.0',port=5000)