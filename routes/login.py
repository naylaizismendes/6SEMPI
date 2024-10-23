from flask import Blueprint,render_template,request
login_route=Blueprint('login',__name__)
    
@login_route.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        
        pass
    return render_template('login.html')