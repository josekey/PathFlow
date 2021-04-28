import csv

def load_specimens_TEST():
    test_spec = []
    with open('specimen_test.csv', newline='') as file:
        r = csv.DictReader(file)
        for row in r:
            test_spec.append({'specimen': row['specimen'] , 'checklist': row['checklist'].split("_")})

    return test_spec