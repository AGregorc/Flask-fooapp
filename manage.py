from flask_script import Manager
from fooApp.app import app

manager = Manager(app)
app.config['DEBUG'] = True  # Ensure debugger will load.
# app.config['SERVER_NAME'] = "Agile"

if __name__ == '__main__':
    manager.run()
