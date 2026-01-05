breakfast = {
    "idly" : 200,
    "dosa" : 150,
    "pori" : 400,
    "rost" : 300,
    "special" : 700
}

srt_val = sorted(breakfast, key = (lambda k: breakfast.get(k)))
srt_val_dec = sorted(breakfast, key = (lambda k: breakfast.get(k)), reverse=True)

print(srt_val)
print(srt_val_dec)