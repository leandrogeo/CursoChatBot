def getTextUser (message):
    text=""
    typeMessage=message["type"]

    if typeMessage=="text":
        text=(message["text"])["body"]
    elif typeMessage == "interactive":
        interactiveObeject = message ["interactive"]
        typeInteractive = interactiveObeject ["type"]
        if typeInteractive == "button_reply":
            text= (interactiveObeject["button_reply"])["title"]
        elif typeInteractive == "list_reply":
            text = (interactiveObeject["list_reply"])["title"]
        else:
            print("sin mensaje")
    else :
        print("sin mensaje")
    return text

def TextMessage(text, number):
    data = {
    "messaging_product": "whatsapp",    
    "recipient_type": "individual",
    "to": number,
    "type": "text",
    "text": {
        "preview_url": text,
        "body": "Hola Usuario"
        }
    } 
    return data  

def TextFormat(number):
    data = {
    "messaging_product": "whatsapp",    
    "recipient_type": "individual",
    "to": number,
    "type": "text",
    "text": {
        "body": "*Hola Usuario*    _Cursiva_    - ~Hola~  ```Holaaaa```  "
        }
    } 
    return data  

def ImgMessage(number):
    data = {
    "messaging_product": "whatsapp",    
    "recipient_type": "individual",
    "to": number,
    "type": "image",
    "text": {
        "link": "https://th.bing.com/th/id/R.d63edc647486c1ff95b5dcd32e4f7cb5?rik=A%2bHmfQh%2bcGoVFQ&pid=ImgRaw&r=0"
        }
    } 
    return data 