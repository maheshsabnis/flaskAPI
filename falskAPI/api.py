from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root123@localhost/Home'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

def expense_to_dict(expense):
    return {
        'ExpensesId': expense.ExpensesId,
        'ExpensesType': expense.ExpensesType,
        'VendorName': expense.VendorName,
        'AmountPaid': expense.AmountPaid,
        'PaidBy': expense.PaidBy
    }


@app.route('/expenses', methods=['POST'])
def add_expense():
    data = request.get_json()
    expense = Expenses(ExpensesId=data['ExpensesId'], ExpensesType=data['ExpensesType'], VendorName=data[
        'VendorName'],
                       AmountPaid=data['AmountPaid'], PaidBy=data['PaidBy'])
    dblogic.add_expense(expense)
    return jsonify({'message': 'Expense added successfully'})


@app.route('/expenses', methods=['GET'])
def get_all_expenses():
    expenses = dblogic.get_all_expenses()
    return jsonify([expense_to_dict(expense) for expense in expenses])

@app.route('/expenses/<int:expense_id>', methods=['GET'])
def get_expense(expense_id):
    expense = dblogic.get_expense(expense_id)
    return jsonify(expense_to_dict(expense))


@app.route('/expenses/<int:expense_id>', methods=['PUT'])
def update_expense(expense_id):
    data = request.get_json()
    new_expense = Expenses(ExpensesId=data['ExpensesId'], ExpensesType=data['ExpensesType'], VendorName=data['VendorName'],
                           AmountPaid=data['AmountPaid'], PaidBy=data['PaidBy'])
    expense = dblogic.update_expense(expense_id, new_expense)
    return jsonify(expense_to_dict(expense))


@app.route('/expenses/<int:expense_id>', methods=['DELETE'])
def delete_expense(expense_id):
    expense = dblogic.delete_expense(expense_id)
    return jsonify(expense_to_dict(expense))


if __name__ == '__main__':
    from models.expenses import Expenses
    from dblogic.dbapplogic import DbLogic
    dblogic = DbLogic()
    app.run(debug=True)
