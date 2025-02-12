from sqlalchemy import Column, Integer, String

from dblogic.dbapplogic import Base
# The Model class is a subclass of the Base class, which is the declarative base class
# provided by SQLAlchemy. This class represents the Expenses table in the database.

class Expenses(Base):
    __tablename__ = 'Expenses'
    ExpensesId = Column(Integer, primary_key=True)
    ExpensesType = Column(String(100), nullable=False)
    VendorName = Column(String(100), nullable=False)
    AmountPaid = Column(Integer, nullable=False)
    PaidBy = Column(String(100), nullable=False)

    def __repr__(self):
        return (f'<Expenses(ExpensesType={self.ExpensesType}, '
                f'VendorName={self.VendorName}, '
                f'AmountPaid={self.AmountPaid}, PaidBy={self.PaidBy})>')

