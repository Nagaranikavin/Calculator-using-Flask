from flask import Flask,request, render_template

app = Flask(__name__)
#Route
@app.route("/")
def welcome():
    return render_template('indexnw.html')

@app.route("/calc",methods=["POST"])
def calc_operation():
    if request.method=="POST":
        operation=request.json["operation"]
        num1=request.json['num1']
        num2=request.json['num2']
        if operation=="add":
            result=num1+num2
        if operation=="subtract":
            result=num1-num2
        if operation=="multiply":
            result=num1*num2
        if operation=="Divide":
            result=num1/num2
        return "The result is {}".format(result)

@app.route("/operation",methods=["POST"])
def math_operation():
    if request.method=="POST":
        operation=request.form["operation"]
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        if operation=="add":
            result=num1+num2
        if operation=="subtract":
            result=num1-num2
        if operation=="multiply":
            result=num1*num2
        if operation=="divide":
            result=num1/num2
        return render_template('resultnw.html',result=result)
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5001)
