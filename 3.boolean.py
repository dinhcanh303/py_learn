list = ["orange", "mango", "kiwi", "pineapple", "banana"]
results = []
for i in list:
    length = len(i)
    results.append(length)
print(results)
value = [x for _,x in sorted(zip(results,list))]

    
    

        

    
   