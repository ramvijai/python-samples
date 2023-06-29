def extract_uppercase(phrase):
    return list(filter(str.isupper, phrase))


def extract_lowercase(phrase):
    return list(filter(str.islower, phrase))
