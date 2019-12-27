*****************************************************************************
**********************************CSV FILE***********************************
Before using the 210 reverse proxy server script,
create a csv file with a student's first name, last name, netID and IP address.
For example:

netID,IP_addr
jd123,192.168.x.x
mj321,192.168.x.x

The script handles the first row as column names,
so make sure the first line of the csv file is:

netID,IP_addr

Save the csv as 'isp.csv' in the same file folder as the 210liveservers.py.

*******************************RUNNING SCRIPT*********************************
To use the it210rproxyservers.py script, type:

python it210rproxyservers.py it210-semesteryear

where semester is fall or winter, and year is in the form of 20XX.

After running the command, there should be a new file with the students
reverse proxy servers set up.

*********************************RELOAD NGINX*********************************
Once the new file is there, reload nginx with:

service nginx reload

******************************************************************************
******************************************************************************
