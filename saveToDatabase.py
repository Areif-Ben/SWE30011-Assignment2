import serial 
import MySQLdb
import time

#establish connection to MySQL. You'll have to change this for your database.
dbConn = MySQLdb.connect("localhost","areifben96","password","rfid_read") or die ("could not connect to database")
#open a cursor to the database
cursor = dbConn.cursor()

device = '/dev/ttyACM1' #this will have to be changed to the serial port you are using
try:
  print("Trying..."),device 
  arduino = serial.Serial(device, 9600) 
except: 
  print("Failed to connect on"),device
while True:
    time.sleep(1)
    try:
        data=arduino.readline().decode("utf-8")
        print(data)
        pieces=data.split(" ")
        try:
            cursor=dbConn.cursor()
            cursor.execute("INSERT INTO rfid_data (ID,Member_ID,allowed_members) VALUES (NULL,%s,%s)", (pieces[0],pieces[1]))
            dbConn.commit()
=            cursor.close()
        except MySQLdb.IntegrityError:
            print("failed to insert data")
        finally:
            cursor.close()
    except:
        print("Processing")
    
            
