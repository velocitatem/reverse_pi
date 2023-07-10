import requests
import json
import os

cookie = os.getenv("PI_COOKIE")
def get_response(input_text):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0',
        'Accept': 'text/event-stream',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://pi.ai/talk',
        'X-Api-Version': '3',
        'Content-Type': 'application/json',
        'Origin': 'https://pi.ai',
        'Connection': 'keep-alive',
        'Cookie': cookie,
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-origin',
        'DNT': '1',
        'Sec-GPC': '1',
        'TE': 'trailers',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    data = {"text":input_text}

    response = requests.post('https://pi.ai/api/chat', headers=headers, data=json.dumps(data))

    response_lines = response.text.split("\n")
    response_texts = []
    response_sid = None

    for line in response_lines:
        if line.startswith('data: {"text":"'):
            start = len('data: {"text":')
            end = line.rindex('}')
            text_dict = line[start+1:end-1].strip()
            response_texts.append(text_dict)
        elif line.startswith('data: {"sid":'):
            print(line)
            start = len('data: {"sid":')
            end = line.rindex('}')
            sid_dict = line[start:end-1].strip()
            sid_dict = sid_dict.split(",")[0][1:-1]
            response_sid = sid_dict


    return response_texts, response_sid


import requests
import os

def speak_response(message_sid):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0',
        'Accept': 'audio/webm,audio/ogg,audio/wav,audio/*;q=0.9,application/ogg;q=0.7,video/*;q=0.6,*/*;q=0.5',
        'Accept-Language': 'en-US,en;q=0.5',
        'Range': 'bytes=0-',
        'Connection': 'keep-alive',
        'Referer': 'https://pi.ai/talk',
        'Cookie': cookie,
        'Sec-Fetch-Dest': 'audio',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-origin',
        'DNT': '1',
        'Sec-GPC': '1',
        'Accept-Encoding': 'identity',
        'TE': 'trailers',
    }

    response = requests.get(f'https://pi.ai/api/chat/voice?messageSid={message_sid}&voice=voice4&mode=eager', headers=headers, stream=True)

    # Ensure the request was successful
    if response.status_code == 200:
        # Open a .wav file in write-binary mode
        with open('speak.wav', 'wb') as file:
            # Write the contents of the response to the file
            for chunk in response.iter_content(chunk_size=128):
                file.write(chunk)

        # run command vlc to play the audio file
        os.system("vlc speak.wav --intf dummy --play-and-exit")

    else:
        print("Error: Unable to retrieve audio.")
