import csv

def validateDataSet(filename):
    repeatedIDs = checkUniqueness(filename)
    if(repeatedIDs == set()):
        print("Every matchID is unique!")
    else:
        print("Found", len(repeatedIDs), "repeated match IDs")
        # print("The following matchIDs are repeated:")
        # print(repeatedIDs)

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


def removeDuplicates(filename, new_filename):
    matchIDs = set()
    new_file = open(new_filename, "w")

    with open(filename,"r") as f:
        reader = csv.reader(f,delimiter = ',')
        for row in reader:
            matchID = row[0]
            if matchID not in matchIDs:
                new_file.write('\n')
                new_file.write(','.join(row))
            matchIDs.add(matchID)
    new_file.close()

filename = '../pre-cleaning-dataset.csv'
new_filename = '../post-cleaning-dataset.csv'
validateDataSet(filename)
cleanDataSet(filename, new_filename)