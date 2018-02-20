# Fanghui He, Yining Hua, Yvonne Zhu, Qiaqia Ji
# Code-challenge 3
# Given a dictionary of items and their (integer, positive-valued) item weights
# identify whether or not there is a subset that could fill a Prime Pantry Box to exactly 100% 
# report which items are in the subset

def primePantryV2(items, n_items, total):
    subsets = [[[''] for i in range(total+1)]for j in range(n_items+1)]
    i=1
    for item in items:
        for j in range(total+1):
            if (j==items[item]):
                subsets[i][j] = item.split()
            for index in range(i):
                if subsets[index][j]!=[''] and (items[item]+j)<=total: 
                    for string in subsets[index][j]:
                        subsets[i][items[item]+j] = string.split() 
                    subsets[i][items[item]+j]+=item.split()
        i+=1
    result = []
    count = 0
    for i in range(n_items+1):
        if subsets[i][total] != ['']:
            result.append(subsets[i][total])
            count+=1
    return result 

def main():
    l= {"a":3,"b":2, "c":5, "d": 4, "e": 1}
    total = 5
    print(primePantryV2(l, len(l), total))
     
if __name__ == '__main__':
    main()
