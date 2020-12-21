<<<<<<< HEAD
#Number pattern Horizontal repetetive pattern
# 0 0 0 0 0 0  
# 1 1 1 1 1 1  
# 2 2 2 2 2 2
# 3 3 3 3 3 3
# 4 4 4 4 4 4
# 5 5 5 5 5 5
rows = 6
for num in range(rows):
    for i in range(rows):
        print(num, end=" ")
    print(" ")
print("---------------")
#Number pattern All same no.
# 6 6 6 6 6 6  
# 6 6 6 6 6 6  
# 6 6 6 6 6 6
# 6 6 6 6 6 6
# 6 6 6 6 6 6
# 6 6 6 6 6 6
rows = 6
for num in range(rows):
    for i in range(rows):
        print(rows, end=" ")
    print(" ")
print("---------------")
#Number pattern Horizontal repetetive pattern
# 0 1 2 3 4 5  
# 0 1 2 3 4 5  
# 0 1 2 3 4 5
# 0 1 2 3 4 5
# 0 1 2 3 4 5
# 0 1 2 3 4 5
rows = 6
for num in range(rows):
    for i in range(rows):
        print(i, end=" ")
    print(" ")
print("---------------")
#Number pattern
# 1  
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
rows = 6
for num in range(rows):
    for i in range(num):
        print(num, end=" ")
    print(" ")
print("---------------")
#Number pattern
# 0  
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4
rows = 6
for num in range(rows):
    for i in range(num):
        print(i, end=" ")
    print(" ")
print("---------------")
#print  star Pattern
#  
# #         
# # #       
# # # #     
# # # # #   
rows = 6
for num in range(rows):
    for i in range(num):
        print("#",end =" ")
    print(" ")
print("---------------")
#print  star Pattern
          #
        # #
      # # #
    # # # #
  # # # # #
rows = 6
for row in range(1, rows):
    num = 1
    for j in range(rows, 0, -1):
        if j > row:
            print(" ", end=' ')
        else:
            print("#", end=' ')
            num += 1
    print("")
print("---------------")
    #print  star Pattern like
# # # # #
 # # # #
  # # #
   # #
    #
for num in range(1, 6):
    for i in range(1, 6):
        if num<=i:
             print("#",end =" ")
        else:
            print("",end=" ")
    print(" ")
print("---------------")

#print  star Pattern like
            # # # # #
              # # # #
                # # #
                  # #
                    #
for num in range(1, 6):
    for i in range(1, 6):
        if num<=i:
             print("#",end =" ")
        else:
            print(" ",end=" ")
    print(" ")
print("---------------")
#print  star Pattern like
# # # # # #
# # # # #
# # # #
# # #
# #
#
rows = 6
for i in range( rows ):
    for j in range(rows -i, 0, - 1):
        print("#", end=" ")
    print()
print("---------------")
=======
#print  star Pattern
#  
# #         
# # #       
# # # #     
# # # # #   
for num in range(6):
    for i in range(num):
        print("#",end =" ")
    print(" ")
print("---------------")
    #print  star Pattern like
# # # # #
 # # # #
  # # #
   # #
    #
for num in range(1, 6):
    for i in range(1, 6):
        if num<=i:
             print("#",end =" ")
        else:
            print("",end=" ")
    print(" ")
print("---------------")

#print  star Pattern like
            # # # # #
              # # # #
                # # #
                  # #
                    #
for num in range(1, 6):
    for i in range(1, 6):
        if num<=i:
             print("#",end =" ")
        else:
            print(" ",end=" ")
    print(" ")
print("---------------")
#print  star Pattern like
# # # # # #
# # # # #
# # # #
# # #
# #
#
rows = 6
for i in range( rows ):
    for j in range(rows -i, 0, - 1):
        print("#", end=" ")
    print()
print("---------------")
>>>>>>> 8170bb45957061d2afa628fa838bffb326cb527a
