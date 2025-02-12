

# define the db operations class

class DbOperations:
    # code for methods to perform CRUD operations on Expenses table using Expenses class
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def add_expense(self, expense):
        from models.expenses import Expenses
        session = self.session_factory()
        session.add(expense)
        session.commit()
        session.refresh(expense)  # Re-associate the object with the session
        session.close()
        return expense

    def get_expense(self, expense_id):
        from models.expenses import Expenses
        session = self.session_factory()
        expense = session.query(Expenses).filter_by(ExpensesId=expense_id).first()
        if expense is None:
            session.close()
            raise Exception("No expense found with id: " + str(expense_id))
        session.refresh(expense)  # Re-associate the object with the session
        session.close()
        return expense

    def get_all_expenses(self):
        from models.expenses import Expenses
        session = self.session_factory()
        expenses = session.query(Expenses).all()
        for expense in expenses:
            session.refresh(expense)  # Re-associate each object with the session
        session.close()
        return expenses

    def update_expense(self, expense_id, new_expense):
        from models.expenses import Expenses
        session = self.session_factory()
        expense = session.query(Expenses).filter_by(ExpensesId=expense_id).first()
        if expense is None:
            session.close()
            raise Exception("No expense found with id: " + str(expense_id))
        expense.ExpensesType = new_expense.ExpensesType
        expense.VendorName = new_expense.VendorName
        expense.AmountPaid = new_expense.AmountPaid
        expense.PaidBy = new_expense.PaidBy
        session.commit()
        session.refresh(expense)  # Re-associate the object with the session
        session.close()
        return expense

    def delete_expense(self, expense_id):
        from models.expenses import Expenses
        session = self.session_factory()
        expense = session.query(Expenses).filter_by(ExpensesId=expense_id).first()
        if expense is None:
            session.close()
            raise Exception("No expense found with id: " + str(expense_id))
        session.delete(expense)
        session.commit()
        session.close()
        return expense
