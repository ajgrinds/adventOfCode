import datetime


def days_between(d1, d2):
    if isinstance(d1, str):
        d1 = datetime.datetime.strptime(d1, "%Y-%m-%d").date()
    if isinstance(d2, str):
        d2 = datetime.datetime.strptime(d2, "%Y-%m-%d").date()
    return abs((d2 - d1).days)
