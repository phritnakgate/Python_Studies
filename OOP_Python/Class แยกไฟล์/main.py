from aCCOUNTANT import Accounting
from Programmer import Programmer
from Sale import Sale

account = Accounting('Kong',40000,30)
account._showData()
dev = Programmer('Buikem',20000,'0 year','Python')
dev._showData()
sale = Sale('Nutto',35000,'CNX')
sale._showData()