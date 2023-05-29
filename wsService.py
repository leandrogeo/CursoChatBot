import requests
import json

def SendMessageWs (text,number):
    try:
        print("1")
        token = "EAAC9mPgePD8BAO9MT6Nq9h5cZC4LgDL9SGGiBkdC93xzcCeJvViIkBRM7jChS3t2LXAHe7Ftvt0HarScD2Y9RaC6Su5XNefwkkL3LEGVVFUd254A2YEIt3SKlYaSV2cIZA1vPjx1eRVD9g3YK2GLcC8KmZA4JSlWvWWlGtHkHoeAnzYPDnGyPHLVHFDxyz34DykJgrULsBM0GrwZAd3d67tdPiCYjwyyF9XH7TMfWQZDZD"
        api_url ="https://graph.facebook.com/v16.0/113489701758952/messages"
        data ={
        "messaging_product": "whatsapp",    
        "recipient_type": "individual",
        "to": number,
        "type": "text",
        "text": {
            "body": text
        }
    }


        headers =   {"Content-Type": "application/json","Authorization": "Bearer " + token}
        responde = requests.post(api_url,data = json.dumps(data),headers=headers)
        print(responde)      
        if responde.status_code == 200 :
            print("3.1") 
            return True 
        else:
            print("3.2") 
            return False    
    except Exception as exception :
        print(exception)
        return False
