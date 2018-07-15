
#https://www.geeksforgeeks.org/pancake-sorting/

#1) Start from current size equal to n and reduce current size by one while it’s greater than 1. Let
#the current size be curr_size. Do following for every curr_size
#……a) Find index of the maximum element in arr[0..curr_szie-1]. Let the index be ‘mi’
#……b) Call flip(arr, mi)
#……c) Call flip(arr, curr_size-1)

#find the maximum element
#Move the largest element to top
#Move the largest element to bottom

def sort_stk(arr) :

  def sort_helper(arr, end) :
    if(end > 0) :
      #find the maximum element
      max_idx = get_max_idx(arr, end)
      #Move the largest element to top
      swap(arr, max_idx)
      #Move the largest element to bottom
      swap(arr, end)
      end -= 1
      sort_helper(arr, end)

  end = len(arr) - 1
  sort_helper(arr, end)

def get_max_idx(arr, end) :
  max_idx = 0
  for i in range(1, end+1):
      if(arr[max_idx] < arr[i]) :
        max_idx = i
  return max_idx

def swap(arr, end) :
  strt = 0
  while(strt < end) :
    arr[strt], arr[end] = arr[end], arr[strt]
    strt += 1
    end -= 1


sort_stk([23, 10, 20, 11, 12, 6, 7])

