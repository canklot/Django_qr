from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests

temp_ac_token = "EAAGZBco97Pm8BAGAZAtvvPVfWnLjnIh9Bkcx6lgDcfrZA5lrvl0XcGCkkV92lTzwiWzHqitlqeXZBJ5DHii79TPTqAZBDa5IWzOBW0rzZCmVbWt5YZCG2tDZBHZBgJCGDJSqTZCDbpujBtVaWyMrlZBLISib8grWhKycLKgxBViw524OlOZBgTdGml6y3oZARBoZAaDF7VbECNKen0awZDZD"

def get_media_url(url):
    my_headers = {"Authorization": "Bearer" + " " + temp_ac_token}
    media = requests.get(url,headers=my_headers)
    json_data = json.loads(media.text)
    return json_data["url"]
def download_media(url):
    my_headers = {"Authorization": "Bearer" + " " + temp_ac_token}
    media = requests.get(url,headers=my_headers)
    return media.content

@csrf_exempt
def webhook(request):
    print("got a webhook request ")
    if request.method == "GET":
        face_secret = "attackontitans99"
        verify_token = request.GET.get('hub.verify_token', 'noverifytoken')
        challenge = request.GET.get('hub.challenge', 'nochallange')
        if face_secret == verify_token:
            print("correct token ")
            return HttpResponse(challenge)

    if request.method == "POST":
        if request.headers.get('content-type') == 'application/json':
            json_data = json.loads(request.body)

            with open("jsonlogs.json", 'a', encoding='utf-8') as f:
                f.writelines(json.dumps(json_data) +","+ "\n")


        # Leave a space between Bearer and token
        my_headers = {"Authorization": "Bearer" + " " + temp_ac_token,
                      "Content-Type": "application/json", }

        post_url = "https://graph.facebook.com/v15.0/102627869338297/messages"

        my_template = {
            "name": "hello_world",
            "language": {"code": "en_US"}
        }

        my_data = {
            "messaging_product": "whatsapp",
            "to": "48505122109",
            "type": "template",
            "template": my_template
        }
        if not "messages" in json_data["entry"][0]["changes"][0]["value"]:
            print("status recieved")
            return HttpResponse("")
        message_type = json_data["entry"][0]["changes"][0]["value"]["messages"][0]["type"]
        if message_type == "text" :
                message_recived = json_data["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"]
                print(message_recived)
        elif message_type == "document" :
            media_id = json_data["entry"][0]["changes"][0]["value"]["messages"][0]["document"]["id"]
            media_url = requests.get("https://graph.facebook.com/v15.0/" + media_id, headers= {"Authorization": "Bearer" + " " + temp_ac_token})
            media_url =media_url.url
            print(media_url)
            media_url2 = get_media_url(media_url)
            media= download_media(media_url2)
            with open("downloaded.pdf", 'wb') as f:
                f.write(media)
            message_recived = "file"
        else:
            message_recived = None

        if message_recived == "hi":
            json_to_send = json.dumps(my_data)
            response = requests.post(post_url, data=json_to_send, headers=my_headers)
            content = response.content
            print(content)
            
    # You need to return blank 200 ok mesage to sender to say I revieved the message stop sending it
    return HttpResponse("")