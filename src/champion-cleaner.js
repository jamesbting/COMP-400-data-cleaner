//takes a json file containing all the champion data and outputs a cleaned one with names and keys only
const fs = require('fs')
const ORIGINAL_FILE = "../data/champions.json"
const CLEANED_FILE = "../data/champions-cleaned.json"

function main() {
    const filepath = ORIGINAL_FILE
    const contents = fs.readFileSync(filepath,'utf8')
    const obj = JSON.parse(contents)
    //clean the object
    const cleaned = cleanObject(obj['data'])
    fs.writeFileSync(CLEANED_FILE , JSON.stringify(cleaned), 'utf8')
    console.log('Done')
}

//takes as input a Object representing the full champion dictionary
//for each champion gets the name and key fields and places it into a new Object
//returns the dataset with only the name and id
function cleanObject(obj) {
    const res = {}
    Object.keys(obj).forEach(function(key, index) {
       const id = Number(obj[key]['key'])
       const name = obj[key]['name']
       res[id] = {}
       res[id]['name'] = name
       res[id]['key'] = index
      })
      return res
}


main()