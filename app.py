from flask import Flask, render_template
@app.route('/')
def home():
    return render_template("final.html")
if __name__ == '__main__':
    app.run()