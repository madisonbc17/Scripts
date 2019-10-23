import re
import json

f = open('ips.csv', 'w+')
f.truncate(0)

first_line = 'NetID,ip_address\n'
f.write(first_line)

with open('student.json') as jsondata:
    output = json.load(jsondata)
    for line in output:
        student_ip = []
        student_id = []

        #find the student ip address
        student_ip = re.findall("[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}", line)

        #find the student id
        student_id = re.findall("[a-z]{1,8}[0-9]{1,5}|[a-z]{1,8}", line)

        #create a line for the csv
        if len(student_id) > 0 and len(student_ip) > 0:
            new_line = student_id[0] + ',' + student_ip[0] + '\n'

        else:
            new_line = "N/A,N/A"
        f.write(new_line)

f.close()
