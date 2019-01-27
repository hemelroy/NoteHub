import requests
import time
import pyimgur


def conversion(directory):
    CLIENT_ID = "11b5e4b7afdaeaf"
    PATH = directory

    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
    print(uploaded_image.title)
    print(uploaded_image.datetime)
    link = uploaded_image.link

    handwriting_key = "9084f3a34c414270b64f049cfeca9141"
    voice_key = "111dc84209ab402c93cc7730dcbeb1b5"

    handwriting_url = "https://eastus.api.cognitive.microsoft.com/vision/v2.0/recognizeText?mode=Handwritten"
    voice_token_url = "https://eastus.api.cognitive.microsoft.com/sts/v1.0/issueToken"
    voice_url = "https://eastus.tts.speech.microsoft.com/cognitiveservices/v1"

    handwriting_post_headers = {
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": handwriting_key
    }

    handwriting_get_headers = {
        "Ocp-Apim-Subscription-Key": handwriting_key
    }

    post_voice_token_headers = {
        "Ocp-Apim-Subscription-Key": voice_key,
        "Host": "eastus.api.cognitive.microsoft.com",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "0"
    }

    post_voice_headers = {
        "X-Microsoft-OutputFormat": "audio-16khz-64kbitrate-mono-mp3",
        "Content-Type": "application/ssml+xml",
        "Host": "eastus.tts.speech.microsoft.com"
    }

    def image_to_text(image_url):
        data = {
            "url": image_url
        }

        handwriting_callback_response = requests.post(handwriting_url, json=data, headers=handwriting_post_headers)
        handwriting_callback = handwriting_callback_response.headers['Operation-Location']

        time.sleep(10)

        handwriting_response = requests.get(handwriting_callback, headers=handwriting_get_headers)

        handwriting_json = handwriting_response.json()

        handwriting_text = ""
        for line in handwriting_json['recognitionResult']['lines']:
            handwriting_text += line['text']

        #print(handwriting_text)
        return handwriting_text

    def text_to_speech(text):
        token_response = requests.post(voice_token_url, headers=post_voice_token_headers)
        post_voice_headers['Authorization'] = "Bearer " + token_response.text.strip()
        
        data = """<speak version='1.0' xml:lang='en-US'><voice xml:lang='en-US' xml:gender='Female'
        name='Microsoft Server Speech Text to Speech Voice (en-US, ZiraRUS)'>""" + text + """</voice></speak>"""

        audio = requests.post(voice_url, data=data, headers=post_voice_headers)

        audio.raise_for_status()

        with open('output.mp3', 'wb') as handle:
            for block in audio.iter_content(1024):
                handle.write(block)


    text = image_to_text(link)
    f = open("textmodel.txt", 'w')
    f.write(text)
    f.close()
    print(text)
    return text 

