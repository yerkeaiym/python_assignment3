# Pyton_Assignment3
## Title:
Assignment_3 Connect with SQL
## Installation

PyPI
```bash
pip install request
pip install flask
pip install jwt
```
or from source
```bash
request - https://pypi.org/project/requests/
jwt - https://pyjwt.readthedocs.io/en/stable/
flask - https://flask.palletsprojects.com/en/2.0.x/
```
## Usage
```bash
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:erkeaiym2408@localhost/users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'thisismyflasksecretkey'
```
## Examples
Outputs will be like these:
```bash
Could not find user with a login : {{data}}
Hello, token which is provided is correct 
Could not verify token
Token : {{data}}
```
Our tokens saved in database
## License
[MIT](https://choosealicense.com/licenses/mit/)
