from kra import Payroll
import psycopg2
from flask import Flask, request, render_template, Request, redirect, url_for, flash,session
from datetime import date
import json, ast
from functools import wraps
app = Flask(__name__)
app.config["SECRET_KEY"] = "#deno0707@mwangi"
conn = psycopg2.connect(database="d2k5vndho8dq5q", host="ec2-54-73-68-39.eu-west-1.compute.amazonaws.com", user="yrkgpwbfaetmsy", port=5432, password="a733ffdb5fba93539455472a035bdb4f931c125d99c5c7cede2ebd9fef7203c4")

@app.route('/',methods=["POST","GET"])
def netpay():
    z=[]
    if request.method=="POST":
        name=request.form["name"]
        basic=request.form["basic"]
        benefits=request.form["benefits"]
        p=(int(basic))
        o=(int(benefits))
        x=Payroll(p,o)
        data = {"name":name,"gross_salary":x.gross_salary,"nssf":x.nssf_var,"taxable":x.taxable_pay,"paye":x.paye,"nhif":x.nhif,"deductions":x.deductions,"netpay":x.net_salary}
        return redirect(url_for('netpay', x=data) )
        
    else:
        
        try:  
            x= request.args['x']                                  
            d = ast.literal_eval(x)                      
            return render_template("kra.html",d=d)
        except:
            if request.method=="GET":
                d={}            
                return render_template("kra.html",d=d)
            else:
                return render_template("kra.html",d=d)





if __name__ == "__main__":
    app.run(debug=True)
