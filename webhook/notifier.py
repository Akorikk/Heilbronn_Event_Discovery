import requests

WEBHOOK_URL = "https://webhook.site/68faa693-c251-40fc-9a92-9182ac03c987"   # change later if needed


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