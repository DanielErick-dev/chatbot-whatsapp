from fastapi import FastAPI, Request
from message_buffer import buffer_message
app = FastAPI()


@app.post("/webhook/{event_type}")
async def webhook(request: Request, event_type: str):
    webhook_data = await request.json()
    try:
        data = webhook_data.get("data", {})
        chat_id = data.get("key", {}).get("remoteJid", "")
        is_from_me = data.get("key", {}).get("fromMe", False)

        if "@g.us" in chat_id or is_from_me:
            return {"status": "ignored"}

        message_data = data.get("message", {})
        message_text = message_data.get("conversation") or \
            message_data.get("extendedTextMessage", {}).get("text")
        if chat_id and message_text:
            await buffer_message(
                chat_id=chat_id,
                message=message_text
            )
    except Exception as e:
        print(f"Erro ao processar o webhook: {e}")

    return {'status': 'ok'}
