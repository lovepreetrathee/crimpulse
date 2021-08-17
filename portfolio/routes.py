from portfolio import app
import re
from flask import render_template, url_for,redirect,request
@app.route("/",methods=["POST","GET"])
def index():
    db={'a':'A','b':'B','c':"C",'d':"D",'e':"E"}
    if request.method=="POST":
        data_to_search=request.form.get('search')
        key_list=[]
        value_list=[]
        for i in db:
            if data_to_search in i:
                key_list.append(i)
                value_list.append(db[i])

        if len(key_list)==0:
            key_list.append("Data not found")
            value_list.append("Data not found")
    
        return render_template('layout.html',key_list=key_list, value_list=value_list)


    return render_template('layout.html')

