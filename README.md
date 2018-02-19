**LOGS ANALYSIS**
*Author - Bobby Newton*

***How to Run:***

Prerequisites:
[Python](https://www.python.org/downloads/)
[Vagrant](https://www.vagrantup.com/)
[VirtualBox](https://www.virtualbox.org/)

**To Run**

Launch Vagrant VM by running vagrant up, you can the log in with vagrant ssh

To load the data, use the command psql -d news -f newsdata.sql to connect a database and run the necessary SQL statements.

The database includes three tables:

Authors table
Articles table
Log table
To execute the program, run python logs.py from the command line.

The logs.py calls the queries from the query1.sql, query2.sql and query3.sql files.
Please ensure these files are together in the same folder with the logs.py.
