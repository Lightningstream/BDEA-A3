relations_file = open('twitter_combined.txt', 'r')
lines = relations_file.readlines()

relations = []
users = set()
# Strips the newline character
for line in lines:
    line = line.replace('\n','')
    id1, id2 = line.split(' ')
    users.add(id1)
    users.add(id2)
    relations.append([id1, id2])

header = "userId:ID,name,:Label\n"
body = ""
count = 0
for user in users:
    body += user + ",user" + str(count) + ",USER\n"
    count += 1
csv_content = header + body[:-1]

f = open("users.csv", "w")
f.write(csv_content)
f.close()

f = open("relations.csv", "w")
f.write(":START_ID,:END_ID,:TYPE\n")
for relation in relations:
    f.write(relation[0] + "," + relation[1] + ",FOLLOWS\n")
f.close()