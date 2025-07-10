import requests
from config import (
    EVOLUTION_API_URL,
    EVOLUTION_INSTANCE_NAME,
    EVOLUTION_AUTHENTICATION_API_KEY
)


def send_whatsapp_message(number, text):
    url = f"{EVOLUTION_API_URL}/message/sendText/{EVOLUTION_INSTANCE_NAME}"
    headers = {
        'apikey': EVOLUTION_AUTHENTICATION_API_KEY,
        'Content-Type': 'application/json'
    }
    payload = {
        'number': number,
        'textMessage': {
            'text': text
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    try:
        response.raise_for_status()
    except Exception as e:
        print(f"Erro ao enviar mensagem via Evolution API: {e}")
        print(f"Response: {response.text}")
