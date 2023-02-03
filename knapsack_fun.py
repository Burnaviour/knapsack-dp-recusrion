
#copyrights machine Muzafar

#COMMENT OUT THE TEST CASE  TO CHECK OUTPUT OT ENTER ANY INPUT W ,w and vi(values)
l=[]#list for item track
#test case 1
# w = [1,2,5,6,7]#weight of items
# vi = [1,6,18,22,28]#cost of items
# W=11
#test case 2
# vi = [ 60, 100, 120 ]
# w = [ 10, 20, 30 ]
# W = 50
#test case 3
# w = [25, 20, 30]#weight of items
# vi = [20, 25,40]#cost of items
# W=50
#test case 3
w = [4,3,5]
vi = [2,5,7]
W=10


n = len(vi)
rows, cols = (n, W+1)
v = [[-1] * cols for i in range(rows)]##2d array
for i in range(len(v)):#filing 2d array

    for j in range(len(v[i])):
        if i >=0 and j == 0:

            v[i][j] = 0
        if i == 0 and j >= 1 and j>=w[0]:
            v[i][j] = vi[0]




def knapsack(n,W):#complaxity O(n*W)

    if n == 0:

        return 0
    if W==0:

        return 0

    if w[n] > W:
        if v[n-1][W] == -1:
            v[n-1][W] = knapsack(n-1,W)
        v[n][W]=v[n-1][W]

        return v[n-1][W]
    
    if(w[n] <=  W):
        # print(f"wight of item is{w[n]} capacity {W} ")

        if v[n-1][W] == -1:
            v[n-1][W] = knapsack(n-1,W)

        if v[n-1][W-w[n]] == -1:
            v[n-1][W-w[n]] = knapsack(n-1,W-w[n])
        v[n][W]=max(v[n-1][W],vi[n]+v[n-1][W-w[n]])
        return v[n][W]

def display():#O(n)
    for i in range(len(v)):
        for j in range(len(v[i])):
            print(v[i][j], end=' ')
        print()
def printitem(result):


    wt = W
    for i in range(n-1, -1, -1):
        if result<= 0:
            break

        if result== v[i - 1][wt]:
            continue
        else:

            l.append(w.index(w[i])+1)#store item in list

            result= result-vi[i]
            wt = wt - w[i]


result=knapsack(len(vi)-1,W)#call knapsack
for i in range(len(v)):

    for j in range(len(v[i])):
        if v[i][j] ==-1:
            knapsack(i,j)

print("\nhere is the 2d array filled by knapsack:\n")
display()
print(f"\nResult of knapsack is :{result}")
##printing items function call for item identification
printitem(result)
print(f"\nlist of item that are in knapasack are: {sorted(l)}")
