# for i in range(80, 5820 + 140, 140):

    # print(i)
    #print(int(i-80)/140)
# result=[]
# row=['1490', '1050', '90', '550']
# rows = [int(i) for i in row ]
# for i, p in zip(sorted(rows), range(len(rows))):
#     print(i,p)

cols=[2180, 1470, 4000, 3020, 360, 1620, 2040, 4980, 4690, 1750, 3860, 3300, 780, 5540, 3580, 4140, 5400, 220, 4560, 1060, 5390, 5250, 1200, 2600, 3160, 2740, 4280, 5120, 2880, 4700, 2320, 3850, 1900, 5260, 2460, 4420, 4550, 910, 3720, 4840, 3570, 500, 1760, 80, 3440, 1480, 5110, 3290, 3010, 2870, 640, 2030, 5680, 920, 1340, 5820]
for i in sorted(cols):
    print(i,(i-80)/140)