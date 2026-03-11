def parse_event(raw_event):

    text = raw_event["raw_text"]
    source_url = raw_event["source_url"]

    lines = [line.strip() for line in text.split("\n") if line.strip()]

    title = None
    date = None
    time = None
    location = None
    description = None

    # Date
    if len(lines) > 0:
        date = lines[0]

    # Title
    if len(lines) > 2:
        title = lines[2]

    # Time + location
    for i, line in enumerate(lines):

        if "Uhr" in line:
            time = line

            if i + 1 < len(lines):
                location = lines[i + 1]

            if i + 2 < len(lines):
                description = lines[i + 2]

            break

    return {
        "title": title,
        "date": date,
        "time": time,
        "location": location,
        "description": description,
        "source_url": source_url
    }