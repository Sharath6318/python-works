hacker_rak=[
    {"name":"abijith","count":4},
    {"name":"adith","count":2},
    {"name":"aadith","count":5},
    {"name":"adwaith","count":4},
    {"name":"amala","count":9},
    {"name":"arun","count":7},
    {"name":"ashiq","count":9},
    {"name":"fayaz","count":0},
    {"name":"felix","count":5},
    {"name":"harshit","count":4},
    {"name":"neenu","count":8},
    {"name":"saniya","count":7},
    {"name":"sarath","count":9},
    {"name":"SIVANANDANA","count":6},
    {"name":"sona","count":7},
    {"name":"vivek","count":2},
    {"name":"vrinda","count":7},
]

sort_by_count = sorted(hacker_rak, key = lambda dict : dict.get("count"))

print(sort_by_count)



