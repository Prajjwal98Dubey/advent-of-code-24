# day4 part1
def counto_of_xmas(grid):
    ROWS,COLS = len(grid),len(grid[0])
    def find_number_of_xmas_from_curr(row,col):
        count = 0
        for nrows,ncols in [[1,0],[0,1],[-1,0],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]:
            r,c = row,col
            t = ""
            for _ in range(3):
                r+=nrows
                c+=ncols
                if r>=0 and r < ROWS and c>=0 and c < COLS:
                    t+=grid[r][c]
            if t == "MAS":
                count+=1
        return count
    cnt = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "X":
                cnt+=find_number_of_xmas_from_curr(r,c)
    return cnt

#day4 part2
def find_x_shape(grid):
    ROWS,COLS = len(grid),len(grid[0])
    def find_shapes(row,col):
        t1,t2= "",""
        # (row-1,col-1) , (row+1,col+1)
        if row-1 >= 0 and col-1 >= 0 and row+1 < ROWS and col+1 < COLS:
            t1=grid[row-1][col-1] + grid[row][col] + grid[row+1][col+1]
        # (row+1,col-1) (row-1,col+1)
        if row+1 < ROWS and col-1 >= 0 and row-1 >= 0 and col+1 < COLS:
            t2 = grid[row+1][col-1] + grid[row][col] + grid[row-1][col+1]
        if (t1=="MAS" or t1=="SAM") and (t2 == "MAS" or t2 == "SAM"):
            return True
        return False
    cnt = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "A":
                if find_shapes(r,c):
                    cnt+=1
    return cnt
def main():
    matrix = []
    while True:
        line = input()
        if line == "":
            break
        else:
            matrix.append([line[i] for i in range(len(line))])
    ans = counto_of_xmas(matrix)  # Day4 part1
    ans = find_x_shape(matrix) # Day4 part2
    return ans
print(main())

'''
Tips for input:
- after writing down the input press enter for coming to "next line" and then again press enter to get the result.
'''