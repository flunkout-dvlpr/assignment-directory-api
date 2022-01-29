# LFL Directory API Assignment

For this assignment you will be building an API to support an online employee
phone directory. 

1. Please fork this repository and work on a copy on your own Github account.
2. Read the assignment below and add the code needed to satisfy the
   requirements.
3. Treat this like a real project and that you are working on a team. Use good
   coding habits, write useful commit messages, and ensure that you document
   what is necessary to understand and run your code.
4. Add any notes about difficulties you had or choices that you made under the
   `Dev Notes` section in this README.
5. When you are done, push your changes to your repo and send the link back to the
   recruiter. 

You are not required to deploy your code, but you are expected to make sure it
works. You should spend no more than 4-6 hours on this assignment and if you
have questions, please ask the recruiter.

# Instructions

We have provided base sample code for a simple Flask server to get you started,
but you will need to add and modify it to fit your needs. You may change
anything you would like to change. 

## Required functions

You are to create a working Python API server that has routes that fulfill all
of the following features:

- List all employees
- Add a new employee
- Update an existing employees name or phone number
- Delete an existing employee

You need to only create the server and do not need to add any frontend UI to
this.

## Data

Each employee should have at minimum two fields:

- name
- phone number (eg "212-555-0000")

We have provided basic sample data in the file `starter-data.json` as an
example. 

## Persistance

You must find a way to persist the data between calls and server restarts. How
you do it is up to you, but please be mindful to document any requirements or
dependencies. 

## Improvements

What improvements could you make to this application code? Be critical - the
starter code is not perfect. If this were a real project, what you would like to
see?

You do not have to implement all of these ideas, but please list out ways
you would go about improving it and then implement at least a few:

- Add your ideas here

# Setup and running

1. Install dependencies with `pip install -R -U requirements.txt`
2. Run with `python app.py`

# Testing

Please explain how your code can be tested.

# Dev Notes
