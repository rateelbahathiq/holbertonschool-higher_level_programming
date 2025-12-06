#!/usr/bin/python3
def multiple_returns(sentence):
    """Return tuple with length of string and first character."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
