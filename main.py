import csv
import json
import trainingjsonfile
import os

# Define The folder name
csvfile = "TrainingCSV/Templet.csv"

# Define the Folder name where you want to create all the JSON file.
importFolder="Intent/"

with open(csvfile, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader, None)
    for row in reader:
        # trainingjsonfile.userSays(row)
        # print(trainingjsonfile.userSays(row))
        
        if row[5]:
            with open(importFolder+row[0]+".json",'w', encoding='utf-8') as f:
                json.dump(trainingjsonfile.defaultcontext(row), f, indent=2, ensure_ascii=False)
        else:
            if(row[10]):
                with open(importFolder+row[0]+"_usersays_"+row[10]+".json", 'w', encoding='utf-8') as f:
                    json.dump(trainingjsonfile.userSays(row), f, indent=2, ensure_ascii=False)
            else:
                with open(importFolder+row[0]+"_usersays_en.json", 'w', encoding='utf-8') as f:
                    json.dump(trainingjsonfile.userSays(row), f, indent=2, ensure_ascii=False)
                
            if row[3] and row[4] or row[3]:
                trainingjsonfile.outputOutputContext(row)
                print(trainingjsonfile.outputOutputContext(row))
                with open(importFolder+row[0]+".json", 'w', encoding='utf-8') as f:
                    json.dump(trainingjsonfile.outputOutputContext(row), f, indent=2, ensure_ascii=False)
            elif row[4]:
                trainingjsonfile.outputContext(row)
                print(trainingjsonfile.outputContext(row))
                with open(importFolder+row[0]+".json", 'w', encoding='utf-8') as f:
                    json.dump(trainingjsonfile.outputContext(row), f, indent=2, ensure_ascii=False)
            else:
                #If the .json file is present it will append the message for different language in the same file.
                if(os.path.exists(importFolder+row[0]+".json")):
                    with open(importFolder+row[0]+".json", encoding="utf8") as f:
                        data = json.load(f)
                    message = {
                                    "type": 0,
                                    "lang": row[10] or "en",
                                            "condition": "",
                                            "speech": row[1]
                                }
                    data['responses'][0]['messages'].append(message)
                    with open(importFolder+row[0]+".json", 'w', encoding='utf-8') as f:
                        json.dump(data, f, indent=2, ensure_ascii=False)
                else:
                    trainingjsonfile.noFollowup(row)
                    with open(importFolder+row[0]+".json", 'w', encoding='utf-8') as f:
                        json.dump(trainingjsonfile.noFollowup(row), f, indent=2, ensure_ascii=False)
