list_year = [2546, 2547, 2548, 2549 ,2550, 2551 , 2552, 2553, 2554, 2555,  2556, 2557, 2558, 2559, 2560, 2561, 2562, 2563 ,2564, 2565 , 2566]
mylist_ =(list(map(str, list_year)))
print(mylist_)

mylist_ = ["พ.ศ. " + x for x in mylist_]
print(mylist_)