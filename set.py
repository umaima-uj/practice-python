set1={"red", "blue", "green"," orange"}
set2={"orange", "purple", "black", "white"}
print(set1.union(set2))

set3=set1.union(set2)
print(set3)

numbers={1,2,3,4,5}
digits={4,5,6,7,8}
print(numbers.intersection(digits))
numbers.intersection_update(digits)
print(numbers)

cities={"karachi", "islamabad", "multan", "lahore" }
cities1={"bangkook","new york", "tokyo", "karachi"}
new_cities =cities.difference(cities1)
print(new_cities)

city=cities.pop()
print(city)
print(cities.isdisjoint(cities1))
print(cities1.issubset(cities))
print(cities.discard("lahore"))
