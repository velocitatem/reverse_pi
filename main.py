import functools
import requests
import enum
import os


class VoiceType(enum.Enum):
    voice1 = "voice1",
    voice2 = "voice2",
    voice3 = "voice3",
    voice4 = "voice4",
    voice5 = "voice5",
    voice5_update = "voice5-update",
    voice6 = "voice6",
    voice7 = "voice7",
    voice8 = "voice8",
    voice9 = "voice9",
    voice10 = "voice10",
    voice11 = "voice11",
    voice12 = "voice12",
    qdpi = "qdpi",


@functools.cache
def get_cookie() -> str:
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
        'Cookie': '__cf_bm: PDXVZica98VlBe6z7Qc7Y4bwOu6qSOa7CC9YHzeF1XU-1713250086-1.0.1.1-5Zqu5T09a_zp0Q12ZN9bzzftJIo.vs6skj0RBCzut_es.HGuyUmcSAGtI3x6pjpbrDlZcwYrFP4luJ4n1qxLdg',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-origin',
        'DNT': '1',
        'Sec-GPC': '1',
        'TE': 'trailers',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    response = requests.post('https://pi.ai/api/chat/start',
                             headers=headers, json={})
    return response.headers['Set-Cookie']


def get_response(input_text, cookie: str = get_cookie()) -> tuple[list[str], list[str]]:
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

    data = {"text": input_text}

    response = requests.post('https://pi.ai/api/chat',
                             headers=headers, json=data)

    response_lines = response.text.split("\n")
    response_texts = []
    response_sids = []

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
            response_sids.append(sid_dict)

    return response_texts, response_sids


def speak_response(message_sid: str, voice: VoiceType = VoiceType.voice4, cookie: str = get_cookie()) -> None:
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

    response = requests.get(f'https://pi.ai/api/chat/voice?messageSid={
                            message_sid}&voice={voice.value[0]}&mode=eager', headers=headers, stream=True)

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
