

def frame():
    print( board[0], " |",board[1],"|",board[2])
    print("---|---|---")
    print( board[3], " |",board[4],"|",board[5])
    print("---|---|---")
    print( board[6], " |",board[7],"|",board[8])

def cheak():
    comb = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in comb:
        if (board[i[0]]==board[i[1]]==board[i[2]]=="X"):
            print("X is won the game")
            return 1
    for i in comb:
        if (board[i[0]] == board[i[1]] == board[i[2]] == "0"):
            print("zero won the game")
            return 1
    return 0

board=["-","-","-","-","-","-","-","-","-"]
frame()
j=0
ans=0
for i in range(9):
    j+=1
    if i%2==0:
        xstep=int(input("enter x position number (count from zero) : "))
        if board[xstep] == "0" or board[xstep] =="X":
            print("not possible")
        else:
            board[xstep] = "X"
        frame()
        ans=cheak()
        if ans==1:
            break
    else:
        zstep = int(input("enter zero position number(count from zero) : "))
        if board[zstep] == "0" or board[zstep] =="X":
            print("not possible")

        else:
            board[zstep] = "0"
        frame()
        ans=cheak()
        if ans==1:
            break
if j==9 and ans!=1:
   print("Game over not won anyone")