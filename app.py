from fastapi import FastAPI, Request

app = FastAPI()


@app.post("/webhook/{event_type}")
async def webhook(request: Request, event_type: str):
    webhook_data = await request.json()
    print(f"Evento recebido: {event_type}")
    print(webhook_data)  # Debug

    try:
        data = webhook_data.get("data", {})
        chat_id = data.get("key", {}).get("remoteJid", "")
        is_from_me = data.get("key", {}).get("fromMe", False)

        if "@g.us" in chat_id or is_from_me:
            return {"status": "ignored"}

        message_data = data.get("message", {})
        message_text = message_data.get("conversation") or message_data.get("extendedTextMessage", {}).get("text")

        if chat_id and message_text:
            number = chat_id.split("@")[0]

            reply_text = f"Oi, tudo bem?\nVocê me mandou a seguinte mensagem:\n\n'{message_text}'"

            from evolution_api import send_whatsapp_message

            send_whatsapp_message(
                number=number,
                text=reply_text
            )
            print(f"Resposta enviada para {number}")

    except Exception as e:
        print(f"Erro ao processar o webhook: {e}")
        print("Dados recebidos que causaram o erro:", webhook_data)

    return {'status': 'ok'}
