from flask import Flask,render_template,request,session,redirect,url_for
import data_base
aa=data_base.data_base()


app=Flask(__name__)
app.config['SECRET_KEY'] = '1'
@app.route('/log_out')
def log_out():
    return render_template("index.html")

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/admin_login")
def admin_login():
    return render_template("admin_login.html")

@app.route("/admin_login1" ,methods=['POST','GET'])
def admin_login1():
    errno = "your totally wrong"
    if request.method == 'POST':
        if request.form['uname'] == "admin" and request.form['pass'] == 'admin':
            return render_template('admin_home.html')
        else:
            return render_template('admin_login.html', error=errno)
    else:
        return render_template('admin_login.html')

@app.route("/admin_home")
def admin_home():
    return render_template("admin_home.html")

@app.route("/admin_add_team")
def add_team():
    return render_template("admin_add_team.html")

@app.route("/add_team1", methods=['POST','GET'])
def add_team1():
    id=""
    name = request.form['name']
    fname = request.form['fname']
    age = request.form['age']
    number=request.form['number']
    gender = request.form['gender']
    mailid = request.form['mailid']
    address = request.form['workrole']
    role = request.form['workrole']
    work_area = request.form['worlarea']
    uname = request.form['uname']
    passworld = request.form['pass']
    status="0"
    aa.register("INSERT INTO employee VALUES('" + id + "','" + name + "','" + fname + "','" + age + "','" + number + "','" + gender + "','" + mailid + "','" + address +
                "','" + role + "','" + work_area + "','" + uname + "','" + passworld + "','" + str(status)+ "')")
    return render_template("admin_add_team.html")

@app.route("/admin_view_employee")
def admin_view_employee():
    data=aa.show("SELECT id,name,fname,age,number,gender,mailid,address FROM employee ")
    if data:
        return render_template("admin_view_employee.html", items=data)
    else:
        return render_template("admin_view_employee.html")

@app.route("/edit_employee/<id>")
def edit_employee(id):
    data = aa.show("SELECT * FROM employee where id='"+id+"'")
    return render_template("admin_edit_employee.html",items=data)

@app.route("/update_employee" ,methods=['POST','GET'])
def update_employee():
    id1 = request.form['id']
    name = request.form['name']
    fname = request.form['fname']
    age = request.form['age']
    number = request.form['number']
    gender = request.form['gender']
    mailid = request.form['mailid']
    address = request.form['workrole']
    role = request.form['workrole']
    work_area = request.form['worlarea']
    uname = request.form['uname']
    passworld = request.form['pass']
    aa.register(
        "UPDATE employee SET name='" + name + "',fname='" + fname + "',age='" + age + "',number='" + number + "',gender='" + gender + "',mailid='" + mailid + "',	address='" + address +
        "',	role='" + role + "',w_area='" + work_area + "',uname ='" + uname + "',pass='" + passworld + "' WHERE id='"+str(id1)+"'")
    return redirect('/admin_view_employee')


# @app.route("/update_employee" ,methods=['POST','GET'])
# def update_employee():
#     id =request.form['id']
#     aa.delete("DELETE FROM employee WHERE id='"+id+"'")
#     return "nothing"

@app.route('/admin_view_user')
def view_user():
    data = aa.show("SELECT name,number,email,gender,address FROM user_register ")
    if data:
        return render_template("admin_view_user.html", items=data)
    else:
        return render_template("admin_view_user.html")


@app.route('/admin_view_report')
def admin_view_report():
    data=aa.show("SELECT * FROM feedback WHERE type='employee'")
    data1 = aa.show("SELECT * FROM employee WHERE  status='" + str(1) + "' ")
    return render_template('admin_view_report.html',items=data, item=data1)

@app.route('/admin_update_request/<id>')
def admin_update_request(id):
    aa.register("update employee set status='"+str(0)+"' where id='"+str(id)+"'")
    return redirect('/admin_view_report')

@app.route('/admin_view_feedback')
def admin_view_feedback():
    data = aa.show("SELECT * FROM feedback WHERE type='user'")
    return render_template('admin_view_feedback.html',itmes=data)


#employee
@app.route('/employee_login')
def employee():
    return render_template("employee_login.html")

@app.route('/employee_login1',methods=['POST','GET'])
def employee_login1():
    uname=request.form['uname']
    password=request.form['pass']
    login=aa.show("select * from  employee  where uname='"+uname+"' and pass='"+password+"'")
    if login:
        session['area']=login[0][9]
        session['id']=login[0][0]
        return render_template('employee_home.html')
    else:
        return render_template('user_login.html')

@app.route('/employee_home')
def employee_home():
    return render_template('employee_home.html')

@app.route('/employee_view_user')
def employee_view_user():
    area=session['area']
    data = aa.show("SELECT name,number,email,gender,address FROM user_register WHERE area='"+area+"' ")
    if data:
        return render_template("employee_view_users.html", items=data)
    else:
        return render_template("employee_view_users.html")

@app.route('/employee_allote_time')
def employee_allote_time():
    area=session['area']
    data = aa.show("select * from user_register where area='"+area+"' and status='"+str(1)+"' ")
    return render_template('employee_allote_time.html',items=data)

@app.route('/time_allort' ,methods=["POST","GET"])
def time_allote():
    start=request.form['start']
    end=request.form['end']
    area=session['area']
    aa.register("update user_register set start_date='"+start+"',end_date='"+end+"' where area='"+str(area)+"'")
    return render_template("employee_allote_time.html")

@app.route('/update_time/<id>')
def update_time(id):
    aa.register("update user_register set status='"+str(0)+"' where id='"+str(id)+"'")
    return render_template("employee_allote_time.html")

@app.route('/truck_request/<id>')
def truck_request(id):
    aa.register("update employee set status='"+str(1)+"' where id='"+str(id)+"'")
    return redirect('/employee_report')

@app.route('/employee_report')
def employee_report():
    id=session['id']
    data = aa.show("select * from employee where id='" + str(id) + "'")
    return render_template('employee_report.html',items=data)

@app.route('/employee_report_update', methods=['POST','GET'])
def employee_report_update():
    id=""
    name=request.form['name']
    area=request.form['area']
    report=request.form['content']
    type="employee"
    aa.register("insert into  feedback values('"+id+"','"+type+"','"+name+"','"+report+"','"+area+"','"+str(0)+"')")
    return redirect('/employee_report')

# user part
@app.route('/user_login')
def user_login():
    return render_template("user_login.html")

@app.route('/verifive_login',methods=['POST','GET'])
def verifive_login():
    uname=request.form['uname']
    password=request.form['pass']
    login=aa.show("select * from user_register where uname='"+uname+"' and pass='"+password+"'")
    if login:
        session['userid']=login[0][0]
        return render_template('user_home.html')
    else:
        return render_template('user_login.html')


@app.route('/register_page')
def register_page():
    return render_template('user_register.html')

@app.route('/register', methods=['POST','GET'])
def register():
    id=''
    name=request.form['name']
    number = request.form['number']
    email = request.form['Email']
    gender = request.form['gender']
    address = request.form['address']
    area = request.form['area']
    pincode = request.form['pincode']
    uname=request.form['username']
    Pass = request.form['password']
    status="0"
    aa.register("INSERT INTO user_register VALUES('"+id+"','"+name+"','"+number+"','"+email+"','"+gender+"','"+address+"','"+area+"','"+pincode+"',"
         "'"+uname+"','"+Pass+"','"+status+"','"+status+"','"+status+"')")
    return render_template("user_login.html")

@app.route('/user_home')
def user_home():
    return render_template('user_home.html')

@app.route('/view_time')
def view_time():
    user=session['userid']
    data=aa.show("select * from user_register where id='"+str(user)+"' ")
    return render_template('view_time.html',items=data)

@app.route('/make_request/<id>')
def make_request(id):
    aa.register("update user_register set status='"+str(1)+"' where id='"+str(id)+"'")
    return redirect('/view_time')

@app.route('/give_feedback')
def give_feedback():
    user = session['userid']
    data = aa.show("select * from user_register where id='" + str(user) + "'")
    return render_template('user_give_feedback.html',items=data)


@app.route('/user_feedback_update', methods=['POST','GET'])
def user_feedback_update():
    id=""
    name=request.form['name']
    area=request.form['area']
    report=request.form['content']
    type="user"
    aa.register("insert into  feedback values('"+id+"','"+type+"','"+name+"','"+report+"','"+area+"','"+str(0)+"')")
    return redirect('/give_feedback')

if __name__ == '__main__':
    app.run(debug=True)


