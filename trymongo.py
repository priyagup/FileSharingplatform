import pymongo

client = pymongo.MongoClient("mongodb+srv://priyagup:Codepri%40143@advancedropboxproject-jdfx8.mongodb.net/test?retryWrites=true",ssl=True)

db = client["AdvanceDropboxproject"]
col = db["Credentials"]
my_query = {"uname": "kashif"}
doc=col.find(my_query)
results = []

for x in doc:
	results.append(x)
	print(type(x))
	print(x)
a="kashif12"
if a == doc[0]['pwd']:
	print(results[0])
	print("match")
else:
	print("Errorrrr")