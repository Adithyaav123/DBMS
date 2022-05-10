import pymongo
url="mongodb://localhost:27017/"
c=pymongo.MongoClient(url)
print(c.database_names())
db=c["college"]
coll=db["stud_list"]

print("\n\nQ1:\n")
for x in coll.find({"gender":"female","course":"MCA"}):
	print(x["name"]["fname"]+" "+x["name"]["lname"]+" "+x["course"]+" "+x["gender"])

print("\n\nQ1:\n")
for t in coll.find({"course":"MCA"}).sort("mark",-1).limit(1):
	print(t["name"]["fname"]+" "+t["name"]["lname"]+" "+str(t["mark"]))
print("\n\nQ1:\n")                                                          
for p in coll.find({"gender":"male","grade":"A+"},{"_id":0,"name.fname":1,"name.lname":1,"grade":1,"gender":1}):
	print(p["name"]["fname"]+" "+p["name"]["lname"]+" "+p["grade"]+" "+p["gender"])
print("\n\nQ1:\n")
for q in coll.find().sort("course","Mechanical").sort("mark",-1).limit(3):
	print(q["name"]["fname"]+" "+q["name"]["lname"]+" "+str(q["mark"]))
print("\n\nQ1:\n")
for i in coll.find({"gender":"female"}):
	print(i["name"]["fname"]+" "+i["name"]["lname"]+" "+str(i["mark"]))
print("\n\nQ1:\n")
for i in coll.find({"mark":{'$gt':80,'$lt':90}}):
	print(i["name"]["fname"]+" "+i["name"]["lname"]+" "+i["course"]+" "+str(i["mark"]))
print("\n\nQ1:\n")
for i in coll.find({"name.fname":{'$regex': '^V'}}):
	print(i["name"]["fname"]+" "+i["name"]["lname"])
print("\n\nQ1:\n")
for x in coll.find({"address.city":"Kollam"}):
	print(x["name"]["fname"]+" "+x["name"]["lname"]+" "+x["address"]["city"])
print("\n\nQ1:\n")
for x in coll.find({"address.city":"Thiruvananthapuram"}):
	print(x["name"]["fname"]+" "+x["name"]["lname"]+" "+x["address"]["city"])
print("\n\nQ1:\n")
for x in coll.find({"gender":"female",'$nor':[{"address.city":'Kollam'},{"address.city":'Thiruvananthapuram'}]}):
	print(x["name"]["fname"])







    

