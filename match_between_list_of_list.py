firstdata = [[["key"],["value"]],
              [[2],["two"]],
              [[3],["three"]]]
seconddata = [[["key"],["artimatic"]],
               [[2],["0+2"]],
               [[2],["1+1"]],
               [[3],["0+3"]],
               [[3],["1+2"]],
               [[3],["2+1"]]]


firstdata_dict = {x[0][0]: x[1][0] for x in firstdata}
seconddata_dict = {}

for data in seconddata:

   if not seconddata_dict.has_key(data[0][0]):
       seconddata_dict[data[0][0]] = []
   seconddata_dict[data[0][0]].append(data[1][0])

for key, value in firstdata_dict.items():
    if seconddata_dict.get(key):
       # key match add your algo
       print seconddata_dict[key]