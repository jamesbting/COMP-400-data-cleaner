import csv

def validateDataSet(filename):
    repeatedIDs = checkUniqueness(filename)
    if(repeatedIDs == set()):
        print("Every matchID is unique!")
    else:
        print("Found", len(repeatedIDs), "repeated match IDs")

def checkUniqueness(filename):
    matchIDs = set()
    nonUniqueIDs = set()
    with open(filename,"r") as f:
        reader = csv.reader(f,delimiter = ',')
        for row in reader:
            matchID = row[0]
            if matchID in matchIDs:
                if matchID not in nonUniqueIDs:
                        nonUniqueIDs.add(matchID)
            else:
                matchIDs.add(matchID)
    return nonUniqueIDs

def cleanDataSet(filename, new_filename):
    removeDuplicates(filename, new_filename)

def get_headers(filename = "../../headers.txt"):
    f = open(filename,"r")
    content = f.read()
    f.close()
    return content

def removeDuplicates(filename, new_filename):
    matchIDs = set()
    new_file = open(new_filename, "w")
    new_file.write(get_headers())
    with open(filename,"r") as f:
        reader = csv.reader(f,delimiter = ',')
        for row in reader:
            matchID = row[0]
            if matchID not in matchIDs and len(row) == 1150:
                new_file.write('\n')
                new_file.write(','.join(row))
            matchIDs.add(matchID)
    new_file.close()

filename = '../../data/pre-cleaning-dataset.csv'
new_filename = '../../data/post-cleaning-dataset.csv'
validateDataSet(filename)
cleanDataSet(filename, new_filename)