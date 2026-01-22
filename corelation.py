def severity_from_count(count):
    if count >= 5:
        return "High"
    elif 2 <= count <= 4:
        return "Medium"
    return "Low"
