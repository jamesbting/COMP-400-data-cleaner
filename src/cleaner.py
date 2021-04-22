# this program checks for uniqueness of match IDs and removes the duplicates
import csv


def clean(original_file, new_file):
    checkUniqueness(original_file)
    removeDuplicates(original_file, new_file)


def checkUniqueness(filename):
    matchIDs = set()
    count = 0
    duplicates = 0
    with open(filename, "r") as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            matchID = row[0]
            if matchID not in matchIDs:
                matchIDs.add(matchID)
            else:
                duplicates += 1
            count += 1
    f.close()
    print(f'Found {duplicates} "repeated match IDs out of {count} matches')


# load the headers
def get_headers(filename="../data/headers.txt"):
    f = open(filename, "r")
    content = f.read()
    f.close()
    return content


# remove the duplicate match IDs, and remove the match IDs with incorrect length
def removeDuplicates(filename, new_filename):
    matchIDs = set()
    new_file = open(new_filename, "w")
    new_file.write(get_headers())
    with open(filename, "r") as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            matchID = row[0]
            if matchID not in matchIDs and len(row) == 1150:
                new_file.write('\n')
                new_file.write(','.join(row))
            matchIDs.add(matchID)
    new_file.close()
