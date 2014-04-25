# VIRTUAL MEMORY/POINTERS. WHAT IS GOING ON. 

m = [[0]*3]*3
m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
nums = range(1, 10)

nums_pointer = 0
i = 0 # m_pointer
j = 0 # row_pointer

while i < len(m):
    row = m[i]
    while j < len(row):
        m[i][j] = nums[nums_pointer]
        j += 1
        nums_pointer += 1
    j = 0
    i += 1

print m