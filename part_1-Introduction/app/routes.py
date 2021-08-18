from app import app

@app.route("/index")
@app.route("/")
def index():
    return "Hello, World!"

@app.route("/latihan-flask")
def latihan_flask():
    return "Aku sedang belajar Flask"