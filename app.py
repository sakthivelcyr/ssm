from flask import Flask
import mysql.connector

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

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1 align='center'>Sakthi Super Market</h1>" + "<p>"+str(myresult)+"</p>"

if __name__ == '__main__':
    app.run()
