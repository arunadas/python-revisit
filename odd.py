from datetime import datetime
import time
import random

odds = { 1,3,5,7,9,11,13,15,17,19,21,23,25,27,
29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59}

for i in range(5):

   right_this_minute = datetime.today().minute
   
   #i=i-1
   if right_this_minute in odds:
      print(datetime.today().minute)
      print ( datetime.today().minute ,"This minute is odd")
   else:
      print("not odd") 
   wait_time = random.randint(1,60)      
   time.sleep(wait_time)