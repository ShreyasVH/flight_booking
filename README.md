# Flight Search App

This is the first round - assignment round. We will we developing some cool application here which will test you coding skill and speed.

## Problem Statement:

In this assignment, we need you to code a flight booking app from scratch , implementing access control, security measures and fast flight search and booking for users from source to destination.
In this assignment, we need you to code a flight booking app from scratch. We have two types of potential users 
- Passenger: Who will book tickets from source to destination.
- Flight Companies (like AirIndia, Indigo...): Who will provide flight details and will use our portal to generate some quarterly reports.

You will need to implement following features in phases:
1. Access Control: We need some access control in place where we decide what to show when user is a passenger or flight companies.
2. Security Measures: Like CSRF and CORS which will make our application more robust and attack free.
3. Search and Booking functionality: Where user can search for flight and book according to their convinces.
4. Flight Operations: Where Flight Companies can schedule flights, cancel them. Also, they can see what was the stats of their company in last few months.


This problem statement is divided into 3 sub problems, for which you will be evaluated.
## Sub problem 1: Access Control

This section deals with `auth_manager` app of this django project. Implement database models to store user information along with info about their session and passwords.

Add roles to user like - Flight Companies or Passenger such that every view has granular access control. And employees from a particular flight operator can access only their data.

`Additional`: We also want you implement standard CORS and CSRF practices such that only our frontend can communicate to backend.

## Sub problem 2: Flight Search and Booking

This sections deals with `flight_company` and `passenger` apps.

For flight companies you will need to implement functionalities like maintaining flight, generating quarterly reports. Getting list of passenger just before boarding flight.

For passengers, you will need to implement flight search, bookings and notification systems.

## Sub problem 3: Bonus Sections:

This is section deals with some over the top features. We expect you to implement:

- Shift from fs-based postgres to docker image, create a read and write docker image. Implement a database wrapper such that all your reports and flight search happens through read replica and write operations happens through master database.
- Use caching to improve search results of frequently searched destinations.

## Instructions:

We want you to design database and implement it. Add models in different django app. Every view has some predefined functions with definitions. You will need to complete these functions/views.

- Try to implement as many features as possible. Make sure your assignment is working. You can create more classes and implement standard practices to make your code more modular, faster, maintainable and extensible.
- Try to write production level code including proper naming conventions, documentation, typing, logging, etc, adhering to `PEP-8` guidelines.
- Write all your test cases inside `tests` folder. We will evaluate you on the basis of quality of test cases and test coverage.
- Pre-configured database is `postgres`, but feel free to use any other relational database.
- Write all your assumptions in `assumptions.md` in root level.
- Some part of code are broken, it is intentional and we need you to fix them.
- There is sample flight data in `data` directory. This this just for reference. You can use it directly, populate more data, columns as you want.
- To run test cases in your local setup, you can use `run_local_tests.sh`
- To run test cases in containerized env, you use `run_tests.sh`

## Scoring Criteria:

You will be scored on the basis of:

- Code Quality: Maintainability, Scalability, extensibility.
- Databases management and Queries.
- Containerization of your application.
- Unit Test cases and Coverage
- Code Documentation
- Additional Features (if any)
