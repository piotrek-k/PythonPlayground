To set up:
```
export FLASK_APP=hello.py
flask run
```
(use `set` instead of `export` on Windows)

Entering debug mode:
```
$ export FLASK_ENV=development
$ flask run
```

> This does the following things:
> 1. it activates the debugger
> 2. it activates the automatic reloader
> 3. it enables the debug mode on the Flask application.
