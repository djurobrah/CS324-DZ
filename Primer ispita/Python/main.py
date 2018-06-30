def check_duplicates(listaBrojeva):
    #set brise duplikate, radi samo ako je flat lista []
    return len(listaBrojeva) != len(set(listaBrojeva))


print (check_duplicates([1,2,3,5,8]))
print (check_duplicates([1,2,3,2,8]))
