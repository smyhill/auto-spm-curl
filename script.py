import pandas as pd
import subprocess

# create list to assign headers
header_list = ["LIC", "LOCATION"]
lic_col = header_list[0]
name_col = header_list[1]

# import data from csv and replace spaces with %20
df = pd.read_csv("curl_data.csv", names=header_list)
df.LOCATION = df.LOCATION.str.replace(' ','%20')

# uncomment iterator if break at bottom of loop for testing
iterator = 0
# set output file here to see the results for testing
with open("output.txt", "w") as file:
    for i in range(len(df)):
        url = '"https://speechusage.uc.r.appspot.com/license?'
        lic = df.loc[i, str(lic_col)] 
        name = df.loc[i, str(name_col)] 
        group = "USMC" # set the group
        command = "curl " + url + "license=" + lic + "&name=" + name + "&group=" + group + '"'
        # print, write to output file and send curl command to cmd via subprocess
        print(command)
        file.write(str(command))
        file.write("\n")
        status, output = subprocess.getstatusoutput(command)
        # iterator is for visual tracking and testing purposes
        iterator += 1
        print(iterator)
        #if iterator == 1:
            #break
        
file.close()
