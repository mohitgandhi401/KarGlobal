def combination(L):   
    final_result = []
    for i in range(3):
        for j in range(3):
            for k in range(3):
                  
                # check if the indexes are not
                # same
                if (i!=j and j!=k and i!=k):
                    print(L[i], L[j], L[k])
                    final_result.append(str(L[i])+ str(L[j]) + str(L[k]))
    return final_result