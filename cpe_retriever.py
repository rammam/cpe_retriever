#/usr/bin/python

import sys
import requests

if len(sys.argv) != 2:
    raise Exception("Please specify the COTS input file. Usage : python3 cpe_retriever.py <INPUT.TXT>")

if sys.argv[1] != "*.txt":
    raise Exception("The COTS input file must be in TXT format. Usage : python3 cpe_retriever.py <INPUT.TXT>")


progress=0
lines=0

list = open(sys.argv[1], "r")

for line in open("cots_list.txt").readlines():
    lines += 1
    
f = open("cots_list.csv", "a")

for line in list:

    keywords = line
    raw = requests.get('https://services.nvd.nist.gov/rest/json/cpes/1.0?keyword='+keywords).json()
    i = raw["result"].keys()
    
    try:    
        print(raw["result"]["cpes"][0]["cpe23Uri"])
        
    except:    
        print("No valid CPE Found.")
        
    progress += 1
    sys.stdout.write('\r')
    sys.stdout.write(str(progress)+"/"+str(lines)+" ")
    sys.stdout.flush()
    
    try:    
        f.write(raw["result"]["cpes"][0]["cpe23Uri"]+",")
        
    except:    
        pass
        
list.close
f.close()