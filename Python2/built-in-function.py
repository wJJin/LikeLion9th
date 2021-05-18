str1 = "멋쟁이 사자 사자처럼"
print(str1[0])
print(str1[0:5])

print(len(str1))

print(str1.count("사"))
print(str1.split())
print(str1.split("사"))
print(str1.find("사"))
print(str1.index("사"))

li=['3','1','배가','4','고파요','5','1']
print(li)

li.sort()
print(li)
print(li.count)

pairs = {'잔나비':"뜨거운 여름밤은 가고 남은 건 볼품없지만", '소히':"산책", '홍크':"어쩌면"}
print(pairs)
pairs['스탠딩 에그'] = '휴식'
print(pairs)
del pairs['잔나비']
print(pairs)

v = pairs.get('스탠딩 에그')
print(v)