import json


FORBES = 'forbes_file.json'


def load_json(filename=FORBES):
    """Will load forbes json file."""
    return json.load(open(filename))


def oldest(billionaires):
    """ Return oldest billionaire under 80."""
    oldest = {'age': 0}
    for b in billionaires:
        if b['age'] > oldest['age'] and b['age'] < 80:
            oldest = b
    return 'Oldest: {oldname}, {oldage}'.format(
        oldname=oldest['name'],
        oldage=oldest['age'])


def youngest(billionaires):
    """ Return youngest billionaire under 80."""
    youngest = {'age': 80}
    for b in billionaires:
        if b['age'] < youngest['age'] and b['age'] > 0:
            youngest = b
    return 'Youngest: {youngname}, {youngage}'.format(
        youngname=youngest['name'],
        youngage=youngest['age'])


if __name__ == '__main__':
    print(oldest(FORBES))
    print(youngest(FORBES))
