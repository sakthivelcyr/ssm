from flask import Flask
import mysql.connector

try:
  mydb = mysql.connector.connect(
    host="ssm-mysql.mysql.database.azure.com",
    user="ssm@ssm-mysql",
    password="Sakthi@22",
    autocommit=True,
    database="ssm"
  )

  mycursor = mydb.cursor()

  mycursor.execute("SELECT * FROM login")

  myresult = mycursor.fetchall()

except:
  myresult = "Database not connected"
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1 align='center'>Hello World !</h1>" + "<p>"+str(myresult)+"</p>"

if __name__ == '__main__':
    app.run()
