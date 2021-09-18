import re

deleteRetweet = re.compile(r"RT @\w+?: ", flags=re.ASCII)


def delete_retweet(a: str):
    return deleteRetweet.sub("", a)


deleteMention = re.compile(r"@\w+? ", flags=re.ASCII)


def delete_mention(a: str):
    return deleteMention.sub("", a)


deleteUrl = re.compile(
    r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+$,%#]+)")


def delete_url(a: str):
    return deleteUrl.sub("", a)


deleteSpaceBetweenJapanese = re.compile(r"(\W)\s(\W)", flags=re.ASCII)


def delete_space_between_japanese(a: str):
    return deleteSpaceBetweenJapanese.sub(r"\1\2", a)


def escape_input(a: str):
    return delete_url(delete_mention(delete_retweet(a)))


def escape_output(a: str):
    return delete_space_between_japanese(delete_space_between_japanese(a))
