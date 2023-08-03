from flask import Flask,request,render_template


obj=Flask(__name__)


@obj.route('/')
def welcome():
  return "welcome to Flask"

@obj.route('/cal',methods=["GET"])
def math_operator():
    operation=request.json["oepration"]
    
    
    numbers1=request.json["number1"]
    numbers2=request.json["number2"]
    
    if operation =="add":
        result=numbers1+numbers2
    elif operation =="multiply":
        result=numbers1*numbers2
    elif operation =="division":
        result=numbers1/numbers2
    else:
        result=numbers1-numbers2
     return result
    

print(__name__)

if __name__ == '__main__':
    obj.run()
    