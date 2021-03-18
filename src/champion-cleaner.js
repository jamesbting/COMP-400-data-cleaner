//takes a json file containing all the champion data and outputs a cleaned one with names and keys only
const fs = require('fs')

function main() {
    const filepath = "../../data/champions.json"
    const contents = fs.readFileSync(filepath,'utf8')
    const obj = JSON.parse(contents)
    const cleaned = cleanObject(obj['data'])
    fs.writeFileSync("../../data/champions-cleaned.json", JSON.stringify(cleaned), 'utf8')
}

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