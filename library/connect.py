import sqlite3 as sql # 

dbCon = sql.connect("planetbook/dfe2.db")

dbCursor = dbCon.cursor()
