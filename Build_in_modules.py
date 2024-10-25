# import  http.client
#
# variable = http.client.HTTPConnection("dummyjson.com")
# variable.request(method="get",url="/todos")
#
# response = variable.getresponse()
# print(response.status)
# print(response.headers)
# print(response.read())
# ###########################################################
#
# # import subprocess
# #
# # result = subprocess.run(
# #     args=['git', '--version'],
# #     capture_output=True,
# #     text=True
# # )
# # print(result.stdout)
#
# #######################################################
# import hashlib
#
# password = b'admin123' #b for byte literal
#
# hash_object = hashlib.md5(password)
# print(hash_object.hexdigest())
#
# ############################################################
from idlelib.pyparse import trans

# import csv
# from os import write
#
# with open('data.csv','w') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Name','Age'])
#     writer.writerow(['Muktadir','23'])


##############################################################

import matplotlib.pyplot as plt
from PIL.ImageFont import truetype

x = [0, 1, 2, 3, 4, 3, 2, 1, 0, -1, -2, -3, -4, -3, -2, -1, 0]
y = [4, 3, 2, 1, 0, -1, -2, -3, -4, -3, -2, -1, 0, 1, 2, 3, 4]

plt.plot(x,y)
plt.title("Sample Graph")
plt.xlabel("Time")
plt.ylabel("catch")
plt.grid(True)
plt.savefig("demo_graph.jpg", format='jpg')
plt.show()
