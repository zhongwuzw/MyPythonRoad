import re
str_temp = '{"name": "john", "smith", "paul", "address": "nyc", "chicago", "age": 50, 60}'
index_temp = str_temp.split(',')
temp_flag = 0
temp_list = []
for object in index_temp:
    if object.find(':') != -1:
        if temp_flag == 0:
            temp_count = object.find(':')
            object = object[:temp_count + 1] + '[' + object[temp_count + 1:]+','
            temp_flag = 1;
        else:
            temp_count = object.find(':')
            object = '],' + object[:temp_count + 1] + '[' + object[temp_count + 1:] + ','
    else:
        object = object + ',' 
    temp_list.append(object)
final_str = ''.join(temp_list)
final_str = final_str[:-2] + ']}'
print final_str
        
        