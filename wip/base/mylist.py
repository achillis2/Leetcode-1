# 数组
li = [1, 2, 3]
for i in li:
   print(i)

for i in range(len(li)):
   print(li[i])

#append(self, object, /)
li.append(4)

#copy(self, /)
##相当于li2 = li[:]
li2 = li.copy()

#extend(self, iterable, /)

##前者合并可迭代对象
li2.extend(li)

#index(self, value, start=0, stop=9223372036854775807, /)
##通过元素值查找元素下标（元素值，开始坐标=0,结束坐标=无穷大）
## li2 list search the element 2 starting from position 4 to position 7
li2.index(2,4,7)

#count(self, value, /)
li2.count(1)

#insert(self, index, object, /)
# 7 is inserted before index 1
li2.insert(1,7)

#pop(self, index=-1, /)
# remove the second last element
# return the removed item
li2.pop(-2)

#remove(self, value, /)
# removes the first matching element 2. The second is not removed.
li2.remove(2)

#reverse(self, /)
li2.reverse()

#sort(self, /, *, key=None, reverse=False)
li2.sort(reverse=True)

#clear(self, /)
li2.clear()
