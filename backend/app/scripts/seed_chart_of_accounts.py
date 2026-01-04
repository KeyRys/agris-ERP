from app.core.database import SessionLocal
from app.accounting.models import Account, AccountType, NormalBalance
COA = [
    #Assets
    ("1100", "Cash", AccountType.asset, NormalBalance.debit),
    ("1200", "Accounts Receivable", AccountType.asset, NormalBalance.debit),
    ("1300", "Inventory", AccountType.asset, NormalBalance.debit),
    ("1350", "Work In Progress", AccountType.asset, NormalBalance.debit),
    #Liability
    ("2100", "Accounts Payable", AccountType.liability, NormalBalance.credit),
    #Equity
    ("3100", "Owner Capital", AccountType.equity, NormalBalance.credit),
    ("3200", "Retained Earnings", AccountType.equity, NormalBalance.credit),
    #Revenue
    ("4100", "Product Sales Revenue", AccountType.revenue, NormalBalance.credit),
    #CoGs
    ("5100", "Cost of Goods Sold", AccountType.expense, NormalBalance.debit),
    #Expenses
    ("6100", "Production Expense", AccountType.expense, NormalBalance.debit),
    ("6200", "Delivery Expense", AccountType.expense, NormalBalance.debit),
]

def run():
    db = SessionLocal()
    
    for code, name, acc_type, normal_balance in COA:
        exists = db.query(Account).filter(Account.code == code).first()
        if not exists:
            account = Account(
                code=code,
                name=name,
                type=acc_type,
                normal_balance=normal_balance
            )
            db.add(account)
    
    db.commit()
    db.close()

if __name__ == "__main__":
    run()