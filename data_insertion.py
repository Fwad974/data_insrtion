import json
import mysql.connector

with open('./fa-IR.jsonl', 'r') as json_file:
    json_list = list(json_file)


    
result=[json.loads(json_str) for json_str in json_list]

uts=[[i["utt"],int(i["id"]),0,0] for z,i in enumerate(result)]

import mysql.connector
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",#"password",
        database="DB"
        )
query = """
    INSERT INTO tasks
    (text, HTML,record_count,id)
    VALUES  """

for i in uts:
    query+="('"+i[0]+"', "+str(i[2])+", "+str(i[3])+", "+str(i[1])+"),"

query=query[:-1]

with mydb.cursor() as cursor:
        cursor.execute(query)
        mydb.commit()
