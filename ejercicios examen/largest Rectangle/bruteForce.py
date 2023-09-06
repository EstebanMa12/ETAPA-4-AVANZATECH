def bruteForceAlgorithm(array):
  n = len(array)
  maxArea = 0 
  for i in range(n):
    minHeight=float('inf')
    for j in range(i,n):
      minHeight = min(minHeight,array[j])
      maxArea = max(maxArea,(j-i+1)*minHeight)
    # print(f"min: {minHeight}; max: {maxArea}, array: {array[i:j+1]}")
  return maxArea

def touch_rectangule_max_area(array, index):
    n = len(array)
    maxArea = 0 
    minHeight = float("inf")
    for j in range(index, n):
        minHeight = min(minHeight, array[j])
        maxArea = max(maxArea, (j - index + 1) * minHeight)
        print(f"min: {minHeight}; max :{maxArea},array: {array[j]}")
    return maxArea


if __name__=="__main__":
  import timeit

  array = [2,1,6,6,2,3, 9, 9, 8]
  print(bruteForceAlgorithm(array))
  

  
  print(timeit.timeit(lambda: bruteForceAlgorithm(array), number=10000))