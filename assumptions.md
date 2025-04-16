* an admin user is created before hand. He can approve flight company registrations
* have added a file seed_demo_data.py to add the admin user. Ideally this will not be committed into the git repo
* for reports, the end_time is considered for filtering
* to demonstrate the master slave DB config, only simulation is done using docker and 2 DBs where replication is not yet configured. For production, we would have to ensure that this configuration is correctly setup. Then we can correctly update the db_router file to read from replica db(currently reading also from the master db)
