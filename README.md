# stripe_api
## Before starting work:
- Install virtual environment and activate it using commands
```
$ python -m venv venv
$ source venv/bin/activate
```
- Install django in virtualenv
```
$ pip install django
```
- Create environment variables
```
$ pip install python-dotenv
```
- Create .env file with following content
```
STRIPE_SECRET_KEY = <секретный ключ вашего stripe>
STRIPE_PUBLISHABLE_KEY = <публичный ключ вашего stripe>
```
You can find the keys in your personal account https://dashboard.stripe.com/
- Install Library stripe
```
$ pip install stripe
```
- Migrate to create a base
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

## To populate the database:
- Register on the site https://dashboard.stripe.com/
- Add products, price and description
- Export prices with columns Price_ID, Product_ID, Amount
- Export productc with columns id, Name, Description
- Merge files into one CSV-file by Product_ID
- Add file to project folder
- Run command 

## Now you can run server
```
$ python3 manage.py runserver 
```
