import mysql.connector
import json
from flask import make_response

class user_model():

    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="localhost",user="root",password="Watch@12345",database="flask_tutorial")
            self.cur=self.con.cursor(dictionary=True)
            self.con.autocommit=True
            print("Connection successful")
        except:
            print("DB connection error")

    def user_getall_model(self):
        #Business logic
        self.cur.execute("select * from users")
        result=self.cur.fetchall()
        if len(result)>0:
            return make_response({"payload":result},200)
        else:
            return make_response({"message":"No Data found"},204)

    def user_addone_model(self, data):
        #Business logic

        self.cur.execute(f"INSERT INTO users(name, email, phone, role, password) VALUES('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")

        return make_response({"message":"user created successfully"},201)

    def user_update_model(self, data):
        #Business logic

        self.cur.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}', role='{data['role']}', password='{data['password']}' where id={data['id']} ")

        if self.cur.rowcount>0:
            return make_response({"message":"user updated successfully"},201)
        else:
            return make_response({"message":"No data to update"},202)
    
    def user_delete_model(self, id):
        #Business logic
        # self.cur.execute("select * from users")
        # print(data)

        self.cur.execute(f"DELETE from users where id={id}")

        if self.cur.rowcount>0:
            return make_response({"message":"user deleted successfully"},200)
        else:
            return make_response({"message":"No data to delete"},202)

    def user_patch_model(self,data,id):
        #Business logic

        # self.cur.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}', role='{data['role']}', password='{data['password']}' where id={data['id']} ")
        quer="UPDATE users SET "
        for key in data:
            quer=quer + f"{key}='{data[key]}',"
        quer=quer[:-1] + f"WHERE id={id}"
        self.cur.execute(quer)
        if self.cur.rowcount>0:
            return make_response({"message":"user updated successfully"},201)
        else:
            return make_response({"message":"No data to update"},202)