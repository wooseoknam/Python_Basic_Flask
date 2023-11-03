# user_id = 1

# dic = {
#     'id': f"{user_id}",
#     'name': 'abcde',
#     'age': 15
# }

# with open('user.txt', 'a') as f:
#     data = f'{dic["id"]}    {dic["name"]}    {dic["age"]}'
#     f.write(data)




# import json
  
# details = {'id': f"{user_id}",
#           'name' : 'abcde',
#           'age': 15}
  
# with open('user.txt', 'a') as f:
#      f.write(json.dumps(details))
#      f.write('\n')

# import json

# with open('user.txt', 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         print((eval(line))['id'])


# details={
#             'id' : f"{user_id}",
#             'name' : 'Alice',
#             'age' : 15
#         }
  
# with open("user.txt", 'a') as f: 
#     for key, value in details.items(): 
#         f.write('%s:%s\n' % (key, value))




# with open('user.txt', 'r') as f:
#     users = f.readlines()
#     user_lst = []
#     for user in users:
#         if eval(user)['id'] == '2':
#             user_lst.append(user)
#     print(user_lst[0])




# import numpy as np
# import cv2

# img = cv2.imread('./default.jpg')

# print(img.shape)
# print(img.size)
# print(img.dtype)

# img2 = cv2.imread('./temp.jpg')

# print(img2 is not None)
# print(img2.size)
# print(img2.dtype)


print(not True)
print(True and False)
print(type(1) == int)