import os
r = os.walk(os.getcwd())
# r = os.walk("/Users/juan.quezada/PycharmProjects/pythonProject/")
print(r)
for folder, sub_folders, files in r:
    print("FOLDER" + folder)
    for sb in sub_folders:
        print(sb)
    print("FILES " + str(files))
