# coding=utf-8


"""Loading this module also populates the EMAILS list once."""


EMAILS = []


if not EMAILS:
    with open('emails.txt') as f:
        for line in f:
            stripped = line.strip()
            if stripped and stripped not in EMAILS:
                EMAILS.append(stripped)
