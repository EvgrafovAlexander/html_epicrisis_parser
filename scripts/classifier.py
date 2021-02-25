def classify_by_dict(text: str, classifier: dict) -> str or None:
    for key in classifier.keys():
        for item in classifier[key]:
            if item in text:
                return key
    return None
