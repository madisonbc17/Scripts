import csv
import sys

#This checks if the user called the Python script with the right command
if len(sys.argv) < 2:
        print ('You failed to provide the semester name as input on the command line')
        print ('Use it210-[insert semester with form of winter2019]')
        sys.exit(1)  # abort because of error

#This will take in the new filename the user wants
semester = sys.argv[1]

#This creates the new file based on the filename submitted
file_write = open(semester,'w+')

#This injests the ips.csv file and reads it into the format Nginx requires for a reverse proxy server.
with open('ips.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        #To make sure the right amount of students are added, we keep track with "line_count"
        line_count = 0
        for row in reader:
                print(row)
                #This gets the student's full name
                name = row['First'] + " " + row['Last']
                #This gets the student's Net ID
                netID = row['netID']
                #This gets the student's assigned IP Address
                ip_addr = row['IP_addr']
                file_write.write("#" + name + "\n")
                file_write.write("#Http Server\nserver{\n\tlisten 80;\n\tserver_name " + netID + ".it210.it.et.byu.edu;\n\tlocation / {\n\t\tproxy_pass http://" + ip_addr + ";\n\t\tinclude include.d/nocacheproxy.conf;\n\t}\n}\n")
                file_write.write("#NodeJS Server\nserver{\n\tlisten 80;\n\tserver_name nodejs." + netID + ".it210.it.et.byu.edu;\n\tlocation / {\n\t\tproxy_pass http://" + ip_addr + ":1337;\n\t\tinclude include.d/nocacheproxy.conf;\n\t}\n}\n\n")
                #This will print out the name of the student to make sure they were added
                print(name + " added successfully!")
                line_count += 1
#This statement lets you know how many students were added successfuly.
print ('{} students have reverse proxy servers'.format(line_count))
#This closes the new file and finishes it.
file_write.close()
