a=123

# arr = "asfdasdf"
# print(arr[19])

# print('asdf')
# try:
#     year = int(input("输入年份："))
# except ValueError:
#     print("请输入数字")
#

# try:
#     print(1/'a')
# except Exception as e:
#     print(' %s' %e)

try:
    raise NameError("hello world")
except NameError:
    print("my custom error")