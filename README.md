# auto-spm-curl
A script to automate the process of sending cURL commands to the spm database
--------------------------------------------------------------------------------------
**Author:** Simon Myhill

**Email:** myhillsimon96@gmail.com
--------------------------------------------------------------------------------------

**To use the script do the following:**
- Create a csv file that contains data in this format: _license,location_ with no spaces surrounding the comma **ex: SIMON-PC,OFFICE**
- The data should be formatted in 2 columns license on the left and location on the right
- Name this file _"curl_data.csv"_ and save it in the same directory you intend to run the _"script.py"_
- If you do not change the csv files name you must specify this on **line 10** of the script
- You can change the column header vals on **line 5** but this is mostly arbitrary as I have included references to their list index on **lines 19,20**
- I have included an **iterator**__ variable for testing purposes
- If you would like to test the script on your data before fully running it, uncomment **line 31 and 32**. This will break the loop after one iteration
- Make sure to recomment those lines to to get the full loop results
- Change the value on **line 31** to allow more than one iteration to occur
- The output of the script is saved to a _"output.txt"_ file in the same directory as the script
- You can change the name of the output file on **line 16** to keep old data. Each time the script is run it overwrites the output files content
- To see the output of the whole script without officially sending it to the database comment out **line 27**. This will write all  lines to _"output.txt"_ for your review
