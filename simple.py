from flask import Flask,url_for,session,redirect,Response,request

app=Flask(__name__)
app.secret_key="mysecretkey"

@app.route("/",methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        
        if username=='admin' and password=='admin':
            session['username']=username
            return redirect(url_for('home'))
        else:
            return Response('<h1>Invalid Credentials</h1>')
        
    else:
        return'''
             <h2>login page</h2>
             <form method="post">
             <input type="text" name="username" placeholder="username">
             <input type="password" name="password" placeholder="password">
             <input type="submit" value="login">
             </form>
             '''
@app.route('/home')
def home():
    if 'username' in session:
        return f'''
    <h1>Welcome {session["username"]}</h1>
    <a herf="{url_for('logout')}>logout</a>
    '''
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('login'))        

if __name__=='__main__':
    app.run(debug=True)  