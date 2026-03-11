'''import json
from openai import OpenAI

client = OpenAI()


def extract_event_with_ai(raw_text):

    prompt = f"""
Extract event information from the following text.

Return JSON with fields:
title
date
time
location
description

TEXT:
{raw_text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    content = response.choices[0].message.content

    return json.loads(content)'''