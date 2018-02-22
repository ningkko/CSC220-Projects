# Fanghui He, Yining Hua, Yvonne Zhu, Qiaqia Ji
# Code-challenge 3
# Given a dictionary of items and their (integer, positive-valued) item weights
# identify whether or not there is a subset that could fill a Prime Pantry Box to exactly 100% 
# report which items are in the subset

def primePantry(items, n_items, total):
    #create a table for dynamic programming
    subsets = [[[] for i in range(total+1)]for j in range(n_items+1)]
    i=1
    # loop through each elements
    for item in items:
        #print(i) 
        for j in range(total+1):
            # fill in the number which is the item number itself
            if (j==items[item]) and subsets[i][j] == []:
                subsets[i][j] = item.split()
            # fill in the number which is the item number itself 
            elif (j==items[item]) and subsets[i][j] != []:
                subsets[i][j].append(item.split())
                #print(subsets[i][j])
            for index in range(i):
                if subsets[index][j]!=[] and (items[item]+j)<=total: 
                    #print(subsets[index][j])
                    for list in subsets[index][j]:
                        #print("list: ",list)
                        subsets[i][items[item]+j].append(subsets[index][j]+item.split())#string.split()
                        #print(subsets[i][items[item]+j])
        i+=1
    result = []
    
    for i in range(n_items+1):
        if subsets[i][total] != []:
            result.append(subsets[i][total])
            
    return result 

def main():
    l= {"a":3,"b":2,"c":5,"d":1,"e":2}
    total = 5
    print(primePantry(l, len(l), total))
     
if __name__ == '__main__':
    main()
