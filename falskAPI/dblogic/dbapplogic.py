from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

from dbaccess.dboperations import DbOperations

Base = declarative_base()
class DbLogic:

    def __init__(self):
        from models.expenses import Expenses
        self.DATABASE_CONNECTION = 'mysql+pymysql://root:root123@localhost/Home'
        self.engine = create_engine(self.DATABASE_CONNECTION)
        self.Session = sessionmaker(bind=self.engine)
        self.dboperations = DbOperations(self.Session)
        self.expenses = Expenses

    def add_expense(self, expense):
        return self.dboperations.add_expense(expense)

    def get_expense(self, expense_id):
        return self.dboperations.get_expense(expense_id)

    def get_all_expenses(self):
        return self.dboperations.get_all_expenses()

    def update_expense(self, expense_id, new_expense):
        return self.dboperations.update_expense(expense_id, new_expense)

    def delete_expense(self, expense_id):
        return self.dboperations.delete_expense(expense_id)
