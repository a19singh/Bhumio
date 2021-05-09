from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])
def predict():
    if request.method == 'POST':
        loan_amt = request.form.get('loan_amt')
        ltv = request.form.get('ltv')
        income = request.form.get('income')
        dti = request.form.get('dti')

        with open('Bhumio.pkl','rb') as file:
            rfc = pickle.load(file)

        i = [[int(loan_amt), float(ltv), float(income), float(dti)]]    
        x= rfc.predict(i)
        print(x)
        s = ''
        if x == 1:
            s = 'Loan originated'
        elif x == 2:
            s= 'Application approved but not accepted'
        return render_template('return.html',result=s)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)