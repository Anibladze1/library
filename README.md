# Book GiveAway

## Api To Get or Giveaway Books For Free

The Book Giveaway Service is a platform where users can generously offer books they no longer need and 
pick up books shared by others, all for free. While anyone can browse the collection of available books, 
only registered members can participate in the giving and taking. 
The platform also provides detailed information about each book, including its author, genre, condition, and more. 
Everyone who uses the API can filter books by its genre, author, title and etc.
## Run Locally
To run locally, you need to create a virtual environment and install all the requirements.

### Steps
- Clone The Repo From GitHub
```sh
git clone https://github.com/Anibladze1/library
```

- Create Virtual Environment and Activate it
```sh
python3 -m bin venv venv
```
```sh
source venv/bin/activate
```

### Requirements
Install all required packages with pip
```sh
pip install -r requirements.txt
```

### Start Server
```sh
python manage.py runserver
```

### Run Unit Tests
```sh
python manage.py test users.tests
```