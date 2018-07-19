import re
from html import unescape

from unidecode import unidecode


def clean_whitespaces(text):
    return " ".join(text.split())


def unescape_text(text):
    """
    Convert named and numeric character references to the corresponding unicode
    characters.
    This function use html.unescape()

    Args:
        text (str): text

    Returns:
        str: text after applying html.unescape and unidecode

    """
    return unidecode(unescape(text))


def camel_case_split(identifier):
    matches = re.finditer(
        r'.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)',
        identifier
    )
    return [m.group(0) for m in matches]


HASHTAG_PATTERN = re.compile(r"#(\w+)")
USERNAME_PATTERN = re.compile(
    r"(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9-_.]*[A-Za-z0-9-_]+)"
)
NUMBER_PATTERN = re.compile(
    r"([-+]?)(?(1)|(?:\b))\d+[.,\d]*(?:\b)"
)

def process_hashtags(text):
    for tag in HASHTAG_PATTERN.findall(text):
        print(tag)
        words = " ".join(camel_case_split(tag))
        print("replacing #{} with {}".format(tag, words))
        text = text.replace("#" + tag, words)

    return text


def normalize_username(text):
    text = USERNAME_PATTERN.sub("NORM_USERNAME", text)
    return text


def normalize_number(text):
    text = NUMBER_PATTERN.sub("NORM_NUMBER", text)
    return text
