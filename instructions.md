* unzip the zip file
* Refer the .env_example file and create the .env file. this will act as environment values for the dockerized application
* Run the following command (Ensure that docker is installed)
    ```
    docker compose up -d
    ```
* Now the application will be accessible at http://localhost:8000
* Run the following command to add the admin user
  ```
  docker exec backend-assignment-master-flight_search-1 bash -c "cd flight_search && python manage.py seed_demo_data"
  ```
* Flight company accounts can be created by accessing `http://localhost:8000/flight_company/create`
* The flight companies can be approved by logging in as the admin user created earlier [email - admin@gmail.com, password - Test@123]
* Now you can perform all the activities of flight company like managing operators, managing flights, viewing passengers of flights, downloading quarterly reports
* Passenger accounts can be created by accessing `http://localhost:8000/signup`
* Now you can perform a;; the activities of passengers like searching for flights, managing bookings
  