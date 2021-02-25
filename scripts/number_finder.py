import re


def get_nums_from_text(text: str) -> list or None:
    matches = re.findall(r'\d', text)
    return [int(num) for num in matches] if matches else None
