from flask import Flask, render_template,session,redirect
app=Flask(__name__)
app.secret_key="rootrootboottootbeeboopbeeboop"

@app.route('/')
def visit_count():
    if "count" not in session:
        session["count"] = 0
    session["count"]+=1
    return render_template("index.html")

@app.route('/destroy_session')
def clear():
    session.clear()
    return redirect('/')
    


if __name__=="__main__":
    app.run(debug=True)

