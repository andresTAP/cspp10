from pprint import pprint

#from the pprint module, import the pprint function
#dictionaries!

#dictionaries contain key-value pairs
d = {
#   key   :  value
    "name":"Chen",
    "birthmonth":"August",
    "grade":16
}

# print(d['name'])

schedule = {
    "A":"SE11",
    "F":"SE12",
    "G":"SE10",
    "D":"SE12"
}

lng = {
    "name":"Mr. Chen",
    "school":"Urban Assembly Gateway",
    "money":0,
    "status":"tired",
    "class":"10th grade SE"
}
#adding a key-value pair
lng['sleep'] = 'none'
pprint(lng)
#deleting a key value pair
del lng['name']
pprint(lng)
#change a value
schedule["F"] = "SE9"
print(schedule["F"])
#add a key-value pair where the key is "E" and
#   the value is "holla"
schedule['E'] = "holla"
# print(schedule['E'])

#ONLY checks if it exists as a KEY (not a value)
if "D" in schedule:
    print("is in schedule")
else:
    print("is not in schedule")

#how to check if a value exists?
for key in schedule:
    if schedule[key] == "whatever":
        print("exists as value!")
        break
else: #this only happens if for loop doesnt break
    print("does not exist as value!")

def add_random(d):
    d['random'] = 'new value yay!'

d = {}
pprint(d)
add_random(d)
pprint(d)

