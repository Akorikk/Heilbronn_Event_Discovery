import requests

WEBHOOK_URL = "http://example.com/webhook"   # change later if needed


def send_webhook(event):

    try:

        response = requests.post(
            WEBHOOK_URL,
            json=event,
            timeout=5
        )

        print("Webhook sent:", response.status_code)

    except Exception as e:

        print("Webhook failed:", e)