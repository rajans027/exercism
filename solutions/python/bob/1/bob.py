def response(hey_bob):

    question = hey_bob.strip()

    if question == "":
        return "Fine. Be that way!"
    elif question[-1] == "?" and question.isupper():
        return "Calm down, I know what I'm doing!"
    elif question.isupper():
        return "Whoa, chill out!"
    elif question[-1] == "?":
        return "Sure."
    else:
        return "Whatever."
