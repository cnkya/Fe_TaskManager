
#!/usr/bin/env sh

export FLASK_APP=app/routes.py
export FLASK_ENV=development
export DEBUG=1 # will show more info in the console for trouble shooting

flask run -p 5001 #changes the port to 5001/to use separate ports