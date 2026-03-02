
import csv

# with open("Smartphone_Usage_Productivity_Dataset_50000.csv") as f:
#     regels = f.readlines()



# print(len(regels))

# for regel in regels:
#     print(regel)


with open("Smartphone_Usage_Productivity_Dataset_50000.csv") as f:
    # regels = f.readlines()
    regelsDict = csv.DictReader(f)
    for r in regelsDict:
        print(regelsDict.line_num, r)
    # print(regelsDict.fieldnames)
    # print(len(regels))
    # for regel in regels:
    #     print(regel)

