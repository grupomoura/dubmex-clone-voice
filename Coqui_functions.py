import requests

voices = [
    {"name":"André MotoGarage", "voice_id":"a37fd1f7-bdd0-4fb6-8fad-b978d6825b79"},
    {"name":"Joyce", "voice_id":"2715643d-e07b-45de-9937-117aef5a6065"}
    ]
    

def clone_voice_file(name, file_path):
    url = "https://app.coqui.ai/api/v2/voices/clone-from-file/"

    files = { "file": (file_path, open(file_path, "rb"), "audio/mpeg") }
    payload = { "name": name }
    headers = {
        "accept": "application/json",
        "authorization": "Bearer IrPya9KPZ6P2t8M1b2S3i6gb1mhgK2xYwtxAox0XUgZ14x0kVbcLo3aaMdT8wVzH"
    }

    response = requests.post(url, data=payload, files=files, headers=headers)
    print(response.text)
    return response

def speak_text(voice_id, text, name, speed=1, emotion="Neutral"):

    url = "https://app.coqui.ai/api/v2/samples"

    payload = {
    "voice_id": voice_id,
    "emotion": emotion,
    "name": name,
    "text": text,
    "speed": speed
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer IrPya9KPZ6P2t8M1b2S3i6gb1mhgK2xYwtxAox0XUgZ14x0kVbcLo3aaMdT8wVzH"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)
    return response.text

def XTTS_speak_text(voice_id, text, name, speed=1):
    import requests

    url = "https://app.coqui.ai/api/v2/samples/xtts/render/"
    payload = {
        "speed": speed,
        "voice_id": voice_id,
        "text": text,
        "name": name
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer IrPya9KPZ6P2t8M1b2S3i6gb1mhgK2xYwtxAox0XUgZ14x0kVbcLo3aaMdT8wVzH"
    }

    response = requests.post(url, json=payload, headers=headers)
    print(response.text)
    return response.text

if __name__ == "__main__":
    voice_id="b8481673-c025-458f-8266-bc5d0f915930"
    text="Isso é apenas um teste"
    name="Whinderson"

    XTTS_speak_text(voice_id, text, name, speed=1)

    # name="Whinderson"
    # file_path="voices_origin/Whinderson_Nunes/Whinderson.mp3"

    # XTTS_clone_voice_file(name, file_path)