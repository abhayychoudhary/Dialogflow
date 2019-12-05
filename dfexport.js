const testFolder = './File Name/';
const fs = require('fs');
const path = require('path');
const os = require('os');

// output file in the same folder
const filename = path.join(__dirname, 'output.csv');
const output = [];
fs.readdir(testFolder, (err, files) => {
    files.forEach(file => {
        //   console.log(files);
        let a = testFolder + file
        fs.readFile(a, 'utf8', (err, jsonString) => {
            if (err) {
                console.log("File read failed:", err)
                return
            } else {
                const row = [];
                row.push(file);
                //Checking file consists utterance or not
                if (JSON.parse(jsonString).length > 0) {
                    for (i = 0; i < JSON.parse(jsonString).length; i++) {
                        let str = "";
                        for (let j = 0; j < JSON.parse(jsonString)[i].data.length; j++) {
                            str += JSON.parse(jsonString)[i].data[j].text.replace(","," ");
                        }
                        row.push(str);
                    }
                    output.push(row.join())
                    fs.writeFileSync(filename, output.join(os.EOL));
                } else {
                    console.log(file, "Files Does not have training utterances")
                }
            }
        })

    });

});
