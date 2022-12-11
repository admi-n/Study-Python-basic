#set = collection which is unordered,unindexed.No duplicate values
#无序|不允许任何重复值
utensils = {"fork","spoon","knife","knife","knife"}
dishes = {"bowl","plate","cup","fork"}

#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()

#utensils.update(dishes) #更新新元素
#for x in utensils:
#    print(x)

#dinner_table = utensils.union(dishes)
#for x in dinner_table:
#    print(x)

#print(utensils.difference(dishes))
print(utensils.intersection(dishes))