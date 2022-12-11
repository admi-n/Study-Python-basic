#19dictionaries
#dictionary = A changeable,unordered collection of unique key:value pairs
#             Fast because they use hashing,allow us to access a value quickly

#             key     value
capitals = {'China':'Beijing',
            'USA':'Washington DC',
            'India':'New Dehli',
            'Russia':'Moscow'}

capitals.update({'Germany':'Berlin'}) #更新|可添加和更改
capitals.pop('India') #删除键值对
#.........

#print(capitals['Germany'])
#print(capitals.get('Germany'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

for key,value in capitals.items():
    print(key,value)
