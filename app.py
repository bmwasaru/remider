from flask import Flask
from scheduler import schedule

app = Flask(__name__)
app.config['SECRET_KEY'] = '9nyz0Vur3EohpgEK5ZaBU4aWNFMBqxaJ'

if __name__ == '__main__':
    schedule.run_pending()
    app.run(debug=True)
