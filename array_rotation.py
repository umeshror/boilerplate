
def left_rotation(a, k):
   rotations = k % len(a)
   return a[rotations:] + a[:rotations]

def right_rotation(a, k):
   rotations = k % len(a)
   return a[-rotations:] + a[:-rotations]

arr = [1,2,3,4,5]
right_rotation(arr, 2)
# output: [4, 5, 1, 2, 3]


right_rotation(arr, 2)
# output: [3, 4, 5, 1, 2]

