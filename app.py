from flask import Flask, render_template


app = Flask(__name__)





lista=[]

@app.route("/")
def Inicio():
    return render_template("index.html")

@app.route("/lista.html", methods=["POST"])
def Lista():
    produto = 'picanha'
    lista.append(produto)
    return render_template("lista.html", msg=lista)



if __name__ == "__main__":
        app.run('0.0.0.0')
