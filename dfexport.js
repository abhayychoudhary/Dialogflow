const testFolder = 'File name';
const fs = require('fs');
const path = require('path');
const os = require('os');

// output file in the same folder
const filename = path.join(__dirname, 'output.csv');
const output = [];
// const test = [];
 // holds all rows of data

fs.readdir(testFolder, (err, files) => {
  files.forEach(file => {
    //   console.log(files);
    let a=testFolder+file
      fs.readFile(a, 'utf8', (err, jsonString) => {
        if (err) {
            console.log("File read failed:", err)
            return
        }
        const row = [];
        //console.log('File data:', jsonString) 
        if(JSON.parse(jsonString).length>0)
        {
         for(i=0;i<JSON.parse(jsonString).length;i++) 
         {
          row.push(file);//
            
            let str="";
             for(let j=0;j<JSON.parse(jsonString)[i].data.length;j++)
             {
                 str += JSON.parse(jsonString)[i].data[j].text;
                 
             }
             row.push(str);
            
         }
        output.push(row.join())
        // function transpose(output) {
        //     return Object.keys(output[0]).map(function (c) {
        //         return output.map(function (r) {
        //             return r[c].join(os.EOL);
        //         });
        //     });
        // }
        
        fs.writeFileSync(filename, output.join(os.EOL));
        }
        else{
          console.log(file,"no data")
        }
      })
      
  });

});





