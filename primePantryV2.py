# Coding challenge 3
# Given a dictionary of items and their (integer, positive-valued) item weights
# identify whether or not there is a subset that could fill a Prime Pantry Box to exactly 100%
# report which items are in the subset

import sys
import ast

def check_input(items,n_items,total):
    '''check_input(items,n_items,total)::= returns TRUE if all inputs are valid.
    '''
    if (type(items) is dict) and (type(n_items) is int) and (type(total) is int) and (total!=0) and (n_items!=0):
        return 1
    return 0

def primePantry(items, n_items, total):
    '''primePantry(items, n_items, total)::= looks for a subset of items in the list items, that has a sum of total.
    Method using: dynamic programming
    '''
    #A memory list consisted of empty list, with a (total+1)*(n_items+1) scale.
    #Note: (total+1)(n_items+1) because we have to look up in the previous item, which doesn't
    #exist for the first item. So for avoiding out_of_range...

    subsets = [[[] for i in range(total+1)]for j in range(n_items+1)]
    i=1

    #loop through every item in items
    for item in items:
        #loop through "total" in each unit
        for j in range(total+1):

            if (j==items[item]) and subsets[i][j] == []:
                subsets[i][j].append(item.split())

            elif (j==items[item]) and subsets[i][j] != []:
                subsets[i][j]+=item.split()
            for index in range(i):
                if subsets[index][j]!=[] and (items[item]+j)<=total:

                        list2 = subsets[index][j]
                        for object in subsets[index][j]:
                            if isinstance(object, list):
                                subsets[i][items[item]+j].append(object+item.split())
                            else:
                                subsets[i][items[item]+j].append(object.split())
                                subsets[i][items[item]+j].append(item.split())

        i+=1
    result = []
    # return the closest-without-going-over solutions
    for j in range(total,0,-1):
        for i in range(n_items+1):
            if subsets[i][j] != []:
                for element in subsets[i][j]:
                    result.append(element)
                    
        if result != []:
            break
    if j!= total:
        print("Unable to fulfill your package, the nearest we can get: {0}.".format(j))

    return result



def main():
    
    # this is the dictionary of items
    dictionary = ast.literal_eval(sys.argv[1])

    # this is the number of items
    nItems = eval(sys.argv[2])

    # this is the total you want to reach
    total = eval(sys.argv[3])

    if check_input(items,n_items,total):
        results = (primePantry(items, n_items, total))

        n_solutions = len(results)
        print("{0} possible sets of items: ".format(n_solutions))
        for m in range(n_solutions):
            n_items = len(results[m])
            print("Set{0} -> {1} items: ".format(m+1,n_items))
            for n in range(len(results[m])):
                print("{0}. ".format(n+1)+results[m][n],end=" ")

    else:
        raise ValueError("The input not valid. Check if they're in correct type && total&n_items>0")


if __name__ == '__main__':
    main()
