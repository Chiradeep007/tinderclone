import mysql.connector
class DBHelper:
    def __init__(self):
        try:
            self._conn=mysql.connector.connect(host= "127.0.0.1",user="root",password="",database="tinder")
            self._mycursor=self._conn.cursor()
        except:
            print("Could Not Connect To Database")
            exit()


    def check_login(self,email,password):
        self._mycursor.execute("SELECT * FROM users WHERE email LIKE '{}' AND password LIKE '{}'".format(email, password))
        data = self._mycursor.fetchall()

        return data


    def fetch_userdata(self,user_id):
        self._mycursor.execute("SELECT * FROM users WHERE user_id LIKE '{}'".format(user_id))
        data = self._mycursor.fetchall()

        return data


    def fetch_otheruserdata(self,user_id):
        self._mycursor.execute("SELECT * FROM users WHERE user_id NOT LIKE '{}'".format(user_id))
        data=self._mycursor.fetchall()

        return data


    def update_info(self,name,age,city,dp,user_id):
        try:
            self._mycursor.execute("UPDATE users SET name= '{}',age={},city= '{}',dp= '{}' WHERE user_id LIKE '{}'".format(name,age,city,dp,user_id))
            self._conn.commit()
            return 1
        except:
            return 0



    def insert_proposal(self,proposer_id,proposed_id):
        self._mycursor.execute("SELECT * FROM proposals WHERE proposer_id = {} AND proposed_id = {}".format(proposer_id,proposed_id))
        data = self._mycursor.fetchall()
        if len(data)==0:
            try:
                self._mycursor.execute("INSERT INTO proposals(proposal_id,proposer_id,proposed_id)VALUES(NULL,'{}','{}')".format(proposer_id,proposed_id))
                self._conn.commit()


                return 1
            except:

                return 0
        else:
            return 2


    def fetch_proposals(self,user_id):
        self._mycursor.execute("""SELECT * FROM proposals p JOIN users u
                                ON u.user_id = p.proposer_id
                                WHERE proposed_id = '{}'""".format(user_id))

        data = self._mycursor.fetchall()

        return data


    def fetch_requests(self,user_id):
        self._mycursor.execute("""SELECT * FROM proposals p JOIN users u
                                ON u.user_id = p.proposed_id
                                WHERE proposer_id = '{}'""".format(user_id))

        data = self._mycursor.fetchall()

        return data


    def fetch_matches(self,user_id):
        self._mycursor.execute("""SELECT * FROM proposals JOIN users
                                ON users.user_id = proposals.proposed_id
                                WHERE proposed_id IN(SELECT proposer_id FROM proposals
                                WHERE proposed_id = '{}')AND proposer_id = '{}'""".format(user_id,user_id))

        data = self._mycursor.fetchall()

        return data


    def register(self,name,email,password,age,gender,city,dp):


        try:
            self._mycursor.execute(
                "INSERT INTO users(user_id,name,email,password,age,gender,city,dp)VALUES(NULL,'{}','{}','{}',{},'{}','{}','{}')".format(
                    name, email, password, age, gender, city,dp))
            self._conn.commit()

            return 1

        except:

            return 0















