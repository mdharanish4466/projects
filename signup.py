import os.path

import pandas as pd
from flask import Flask ,render_template,redirect,request,url_for,make_response

app=Flask(__name__, template_folder="templates")

if not os.path.exists("signup.csv"):
    structure={
        "id":[],
        "poll":[],
        "option1":[],
        "option2":[],
        "vote1":[],
        "vote2":[]    }

    pd.DataFrame(structure).set_index("id").to_csv("signup.csv")

polls_df=pd.read_csv("signup.csv").set_index("id")



@app.route("/")
def index():
    return render_template("signup.html",polls=polls_df)

@app.route("/polls/<id>")
def polls(id):
    poll=polls_df.loc[int(id)]
    return render_template("signup_details.html",poll=poll)

@app.route("/polls",methods=["GET","POST"])
def create_poll():
    if request.method=="GET":
        return render_template("signup_new.html")
    elif request.method=="POST":
        poll=request.form['poll']
        option1=request.form['option1']
        option2=request.form['option2']
        polls_df.loc[max(polls_df.index.values)+1]=[poll,option1,option2,0 ,0]
        polls_df.to_csv("signup.csv")
        return redirect(url_for("index"))

@app.route("/vote/<id>/<option>")
def vote(id,option):
  if request.cookies.get(f"vote_(id)_cookie") is None:
      polls_df.at[int(id), "vote" + str(option)] += 1
      polls_df.to_csv("signup.csv")
      response=make_response(redirect(url_for("polls", id=id)))
      response.set_cookie(f"vote_{id}_cookie",str(option))
      return response
  else:
      return "You can vote only Once"

if __name__=="__main__":
    app.run(host="localhost",debug=True)