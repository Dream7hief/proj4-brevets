"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments. 
#


def open_time( control_dist_km, brevet_dist_km, brevet_start_time ):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet in kilometers,
           which must be one of 200, 300, 400, 600, or 1000 (the only official
           ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    open = brevet_start_time
    inc_hours = 0
    inc_minutes = 0
    max_speed = {1000:26, 600:28, 400:30, 200:32, 0:34}
    dstnce_tbl =[1000, 600, 400, 200, 0]

    if control_dist_km <= (1.2*brevet_dist_km): #Check if control point is over 20% more than brevet distance
      for i in range(len(dstnce_tbl)):
        if control_dist_km >= dstnce_tbl[i]:
          speed = max_speed[dstnce_tbl[i]]
          distance =control_dist_km - dstnce_tbl[i]
          time = divmod(distance/speed, 1)
        
          inc_hours += time[0]
          inc_minutes += time[1]
          control_dist_km -= distance

      open = open.replace(hours=+inc_hours)
      open = open.replace(minutes=+round((60*inc_minutes),0))
      
      return open.isoformat()

    else:

      return brevet_start_time.isoformat()

    

def close_time( control_dist_km, brevet_dist_km, brevet_start_time ):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet in kilometers,
           which must be one of 200, 300, 400, 600, or 1000 (the only official
           ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    close = brevet_start_time
    inc_hours = 0
    inc_minutes = 0
    min_speed = {1000:13.333, 600:11.428, 0:15}
    dstnce_tbl =[1000, 600, 0]

    if control_dist_km <= (1.2*brevet_dist_km) and not(control_dist_km==0) : #Check if control point is over 20% more than brevet distance
      for i in range(len(dstnce_tbl)):
        if control_dist_km >= dstnce_tbl[i]:
          speed = min_speed[dstnce_tbl[i]]
          distance =control_dist_km - dstnce_tbl[i]
          time = divmod(distance/speed, 1)
        
          inc_hours += time[0]
          inc_minutes += time[1]
          control_dist_km -= distance

    
      close = close.replace(hours=+inc_hours)
      close = close.replace(minutes=+round((60*inc_minutes),0))
   
      return close.isoformat()

    elif control_dist_km==0:
      close = close.replace(hours=+1) # close time of 0km control is always an hour after start

      return close.isoformat()
    else:

      return brevet_start_time.isoformat()


