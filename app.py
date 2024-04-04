from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def portfolio():
    return render_template('index.html')

@app.route('/contact/',methods=['GET','POST'])
def contact():
    if request.method=='POST':
        name=request.form['name']
        subject=request.form['Subject']
        email=request.form['_replyto']
        message=request.form['message']
        
    return render_template('contact.html',name=name, subject=subject, email=email, message=message)
                
if __name__ == '__main__':
    app.run(debug=True)

