from faker import Faker
import json

a=[]
faker=Faker(locale='zh_CN')
for i in range(1,100):
    a.append({"id":i,"name":faker.name(),"phonenumber":faker.phone_number()})
print(a)
myjson = json.dumps(a,ensure_ascii=False)
print(myjson)
file=open('myjson.json','w',encoding='UTF-8')
file.write(myjson)
file.close()