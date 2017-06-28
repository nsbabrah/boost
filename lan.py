# db a-> nav nav nav nav
#
# a[4] = nav di rows

col = ["username", "id", "autoac_name", "listlike", "image"]
data = [['a1', '2', '3', '4', 5], ['b1', '2', '3', '4', 5], ['c1', '2', '3', '4', 5], ['1d', '2', '3', '4', 5]]
# for i in inst nav:  to make list['1','2','3','4',5]]
#     data.append([i#is row])
temp = []
for i in data:
    temp.append (dict (zip (col, i)))
print temp
