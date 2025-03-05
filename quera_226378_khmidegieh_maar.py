# https://quera.org/problemset/226378
# خمیدگی مار
# 
masir=input()
jadval = [[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]] 
i, j = 1, 0  

#یا مقدار اولیه در جدول به صورت زیر باید گذاشته بشه
# jadval = [[0] * 8, [0] * 8]  
# i, j = 1, 0  
# jadval[i][j] = 1 

for move in masir:
    if move == "L":
        i, j = i - 1, j + 1
    elif move == "F":
        i, j = i, j + 1
    elif move == "R":
        i, j = i + 1, j + 1

    
    if i < 0 or i > 1:
        print("DEATH")
        break
    else:
        jadval[i][j] = 1

else:  
    for row in jadval:
        for cell in row:
            print(cell, end="")
        print()
    
    #نحوه چاپ به روش دیگر
    # for row in jadval:
    #     result = ""
    #     for num in row:
    #         result += str(num)
    #     print(result)



