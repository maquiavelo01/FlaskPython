import mysql.connector

def insertMBTARecord(mbtaList):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MyNewPass",
    database="MBTAdb"
    )

    mycursor = mydb.cursor()
    #complete the following line to add all the fields from the table
    sql = "insert into mbta_buses ( id, latitude, longitude, occupancy_status, current_stop_sequence, direction_id, current_status, speed, updated_at  ) values (%s, %s,%s,%s,%s,%s,%s,%s,%s)"
    for mbtaDict in mbtaList:
        #complete the following line to add all the fields from the table
        val = (mbtaDict['id'], mbtaDict['latitude'],mbtaDict['longitude'],mbtaDict['occupancy_status'],mbtaDict['current_stop_sequence'],mbtaDict['direction_id'],mbtaDict['current_status'],mbtaDict['speed'],mbtaDict['updated_at'])
        mycursor.execute(sql, val)

    mydb.commit()