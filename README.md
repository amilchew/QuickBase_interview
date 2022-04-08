# QuickBase_interview

### The problem
The problem can be found [here](https://github.com/QuickBase/interview-demos/tree/master/python).

### How to run the code? 
Firstly, you should have Python installed on your machine. Then, follow the instructions below: 

  1. Clone the respository

     ``` 
     $ https://github.com/amilchew/QuickBase_interview.git 
     ```
 
  2. Create a virtual environment 

     ``` 
     $ python3 -m venv /path/to/new/virtual/environment
     ``` 
   
  3. Activate venv 

     ```
     $ source ./env/Scripts/activate
     ```
   
  4. Install the requests library 
   
     ```
     $ pip install requests
     ```
   
  5. Run the code
   
     ```
     $ python main.py
     ```
     
### Idea of implementation 
We have several tasks to do while solving this problem. Initially, we have to take the information for the chosen fields (name, email, address, description) from the GitHub account by given username and access token. Then, need to create a new Freshdesk account or update an already existing one with the same information in the corresponding fields (name, email, location, bio). We are doing that by using basic authentication for the Freshdesk API, that is encoding "FRESHDESK_TOKEN:X" in base 64, as described in the Freshdesk API documentation. However, we also have to transform the GitHub data to suitable for Freshdesk one (for that purpose we use JSON).
The idea of unit testing is checking whether the chosen fields contain the same information after the code has been executed in the two accounts, for GitHub the fields (name, email, address, description) corresponding to the Freshdesk (name, email, location, bio).

### ToDo
- Implement unit tests
- Create more tests
- Fix the authentication problem
- Think about optimization 

### Licanse
BSD 3

### Author
Aleksandar Milchev
