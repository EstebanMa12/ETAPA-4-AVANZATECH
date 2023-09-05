def div_and_conquer_method(array):
  def divide_and_conquer(array,low,high):
    if low == high:
      return array[low]
    mid = (low+high)//2
    left = divide_and_conquer(array,low,mid)
    right = divide_and_conquer(array,mid+1,high)
    return max(left,right,merge(array,low,mid,high))
  def merge(array,low,mid,high):
    left = mid
    right = mid+1
    minHeight = min(array[left],array[right])
    maxArea = 2*minHeight
    while left > low or right < high:
      if right < high and (left == low or array[left-1] < array[right+1]):
        right += 1
        minHeight = min(minHeight,array[right])
      else:
        left -= 1
        minHeight = min(minHeight,array[left])
      maxArea = max(maxArea,(right-left+1)*minHeight)
    return maxArea
  return divide_and_conquer(array,0,len(array)-1)

if __name__=="__main__":
  array = [2,1,6,6,2,3]
  print(div_and_conquer_method(array))
