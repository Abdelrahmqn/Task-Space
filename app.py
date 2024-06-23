# !/usr/bin/python3
from website import application


app = application()

if __name__ == "__main__":
    app.run(debug=True)
