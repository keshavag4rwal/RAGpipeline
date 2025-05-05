import re
from datetime import datetime, timedelta

def parse_timestamp(ts):
    """Convert HH:MM:SS or MM:SS to timedelta."""
    parts = list(map(int, ts.split(":")))
    if len(parts) == 2:
        return timedelta(minutes=parts[0], seconds=parts[1])
    elif len(parts) == 3:
        return timedelta(hours=parts[0], minutes=parts[1], seconds=parts[2])
    else:
        return timedelta(0)

def read_transcript(file_path):
    """Read and parse timestamped transcript."""
    pattern = r'\[(\d{2}:\d{2}(?::\d{2})?)\]\s*(.*)'
    entries = []

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            match = re.match(pattern, line.strip())
            if match:
                timestamp, text = match.groups()
                time = parse_timestamp(timestamp)
                entries.append((time, text))
    return entries

def split_into_slots(entries, slot_minutes=2):
    """Split transcript entries into slots of fixed time."""
    slots = []
    slot_duration = timedelta(minutes=slot_minutes)
    current_slot = []
    start_time = timedelta(0)
    end_time = start_time + slot_duration

    for time, text in entries:
        if time < end_time:
            current_slot.append(text)
        else:
            slots.append(" ".join(current_slot))
            current_slot = [text]
            while time >= end_time:
                start_time += slot_duration
                end_time = start_time + slot_duration

    if current_slot:
        slots.append(" ".join(current_slot))

    return slots
