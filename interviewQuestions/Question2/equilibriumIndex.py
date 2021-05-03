

def equilibriumIndex(inArray):
 
    # finding the sum of whole array
    totalSum = sum(inArray)
    leftSum = 0

    for i, num in enumerate(inArray):
        
        # update totalSum to get the right sum.
        # totalSum is now right sum for index i
        totalSum -= num

         
        if leftSum == totalSum:
            return i
        leftSum += num
      
      # If no equilibrium index found,then return -1
    return -1


inArr = [3,5,8,9,0,-1]

find = equilibriumIndex(inArr)

if find == -1:
    print "no equilibrium index found"
else:
    print "The equilibrium index is %s"%find

