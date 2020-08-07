import mysql.connector
conn = mysql.connector.connect(host="127.0.0.1",user = "root",password = "",database = "tinder" )
mycursor = conn.cursor()
#mycursor.execute("DROP DATABASE tinder")
#conn.commit()
#mycursor.execute("CREATE DATABASE tinder")
#conn.commit()

#mycursor.execute("CREATE TABLE proposals (proposal_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, proposer_id INT NOT NULL,proposed_id INT NOT NULL)")
#conn.commit()

#mycursor.execute("INSERT INTO users(user_id,name,email,password,age,gender,city,dp)VALUES(NULL,'Virat Kohli','virat@gmail.com','1234',28,'Male','Mumbai','virat.png')")
#conn.commit()
#mycursor.execute("INSERT INTO users(user_id,name,email,password,age,gender,city,dp)VALUES(NULL,'Rohit Sharma','rohit@gmail.com','rohit',31,'Male','Mumbai','rohit.png')")
#conn.commit()
#mycursor.execute("INSERT INTO users(user_id,name,email,password,age,gender,city,dp)VALUES(NULL,'M.S.Dhoni','dhoni@gmail.com','dhoni',38,'Male','Ranchi','dhoni.png')")
#conn.commit()
#mycursor.execute("INSERT INTO users(user_id,name,email,password,age,gender,city,dp)VALUES(NULL,'Yuvraj Singh','yuvraj@gmail.com','yuvraj',35,'Male','Punjab','yuvraj.png')")
#conn.commit()
#mycursor.execute("INSERT INTO users(user_id,name,email,password,age,gender,city,dp)VALUES(NULL,'Saurav Ganguly','saurav@gmail.com','saurav',44,'Male','Kolkata','saurav.png')")
#conn.commit()
#mycursor.execute("INSERT INTO users(user_id,name,email,password,age,gender,city,dp)VALUES(NULL,'Gautam Gambhir','gautam@gmail.com','gautam',40,'Male','Delhi','gautam.png')")
#conn.commit()
#mycursor.execute("SELECT * FROM users WHERE user_id<=4")
#data=mycursor.fetchall()
#for i in data:
    #print(i[1],i[2])

#mycursor.execute("SELECT * FROM users WHERE name LIKE 'R%'")
#data=mycursor.fetchall()
#print(data)

#mycursor.execute("UPDATE users SET user_id= 10 WHERE user_id=18")
#conn.commit()

#mycursor.execute("UPDATE users SET age= 45 WHERE name LIKE 'S%'")
#conn.commit()

#mycursor.execute("DELETE FROM users WHERE user_id= 6")
#conn.commit()

#mycursor.execute("UPDATE users SET user_id=6 WHERE name LIKE 'G%'")
#conn.commit()






