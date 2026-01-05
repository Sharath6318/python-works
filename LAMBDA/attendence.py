attendance=[
    {"name":"abin","attendance_count":28,"count":1},
    {"name":"aadhil","attendance_count":20,"count":2},
    {"name":"adhnan","attendance_count":20,"count":2},
    {"name":"arya","attendance_count":25,"count":5},
    {"name":"clairin","attendance_count":25,"count":4},
    {"name":"joji","attendance_count":26,"count":7},
    {"name":"libin","attendance_count":28,"count":7},
    {"name":"lijo","attendance_count":21,"count":2},
    {"name":"shajeer","attendance_count":27,"count":2},
    {"name":"shafi","attendance_count":28,"count":7},
    {"name":"resin","attendance_count":24,"count":3},
    {"name":"lakshmi","attendance_count":16,"count":6},
    {"name":"thammana","attendance_count":25,"count":1},
    {"name":"VARSHANA","attendance_count":8,"count":0},
]

# max_attendance_count of name attendance count ................

max_hack_count = max([a.get("attendance_count") for a in attendance])

max_atte_cou_n_c = [{v.get("name") : v.get("attendance_count")} for v in attendance if v.get("attendance_count") == max_hack_count]

print(f"Max attendance count {max_atte_cou_n_c}")



# max hack_count of  name count .....................

srt_by_attendence = sorted(attendance, key = lambda k : k.get("attendance_count"))

max_hack_count = max([c.get("count") for c in srt_by_attendence])

name_hack_count = [{k.get("name") : k.get("count")} for k in srt_by_attendence if k.get("count") == max_hack_count]

print(f"Highest hackRank count : {name_hack_count}")



# lowest attendance count of name attendance count ...................

lowest_attendance_count =  min([a.get("attendance_count") for a in attendance])

lowest_attendance_count_n_c = [{v.get("name") : v.get("attendance_count")} for v in attendance if v.get("attendance_count") == lowest_attendance_count]

print(f"low attendance  {lowest_attendance_count_n_c}")


# Lowest hackrank count.................

least_hack_count = min([c.get("count") for c in attendance])

least_hack_count_n_c = [{v.get("name") : v.get("count")} for v in attendance if v.get("count") == least_hack_count]

print(f"least hack count {least_hack_count_n_c}")


# sort_by_attendance 

sort_by_attendance = sorted(attendance,key = lambda dict : dict.get("attendance_count"))

print(f"Data sort by attendance count wise : {sort_by_attendance}")




















