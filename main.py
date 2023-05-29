from flask import Flask, request
import funciones
import wsService
app = Flask(__name__)

@app.route('/welcome', methods = ['GET'])
def index ():
    return "Bienvenido a mi chat"

@app.route('/whatsapp', methods = ['GET'])
def VerifyToken():
   try:
    accesstoken = "3bg4f56d67fg89x09d"
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if token != None and  challenge != None and token == accesstoken:
        return challenge
    else: 
        return "", 400
   except:
    return "", 400




@app.route('/whatsapp', methods = ['POST'])
def ReceivedMessage():
    try:
       body = request.get_json()
       entry = (body["entry"])[0]
       changes = (entry["changes"])[0]
       value = changes["value"]
       message = (value["messages"])[0]
       number = message["from"]
       text=funciones.getTextUser(message)
       GenerateMessage(text, number)
       print("nuymeroo ", number)
       return "EVENT_RECEIVED"
    except:
        return "EVENT_RECEIVED  s"

def GenerateMessage (text,number):
    print("el usuraio dijo: ", text)
   # if "format" in text:
     #  data=funciones.TextFormat(number) 
    #if "image" in text:
     #  data=funciones.ImgMessage(number) 
    wsService.SendMessageWs(text,number)









if (__name__ == "__main__"):
    app.run()    