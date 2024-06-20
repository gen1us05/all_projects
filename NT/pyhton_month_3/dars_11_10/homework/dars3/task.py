# import os
#
# exclude = ['.idea', "dars2"]
# pasw = ""
# found = False
# path = ''
# for file in os.listdir():
#     if os.path.isdir(file) and file not in exclude:
#         os.chdir(file)
#         for file in os.listdir():
#             with open(file) as f:
#                 for line in f.readlines():
#                     if "password" in line:
#                         found = True
#                         _, pasw = line.split(" ", maxsplit=1)
#             if found:
#                 path = f"{os.getcwd()}/{file}"
#                 found = False
#
#         os.chdir("../../")
# print(pasw)
# print(path)
# try:
#     with open("Dat.yx") as f:
#         pass
# except Exception as e:
#     print(e)
