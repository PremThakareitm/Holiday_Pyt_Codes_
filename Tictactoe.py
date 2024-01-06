# create a tic tac toe game

l=[[1,2,3],[4,5,6],[7,8,9]]

print("\n* Welcome to the Tic-Tac-Toe *\n")
p1=input("Enter Player 1 Name: ")
p2=input("Enter Player 2 Name: ")
max_lenght=3
def board(l):
    print("\n |",l[0][0], "|", l[0][1], "|", l[0][2], "|""\n-+---+---+---+-\n","|",l[1][0], "|", l[1][1], "|", l[1][2], "|""\n-+---+---+---+-\n","|",l[2][0], "|", l[2][1], "|", l[2][2], "|\n")
board(l)
i=[[1,2,3],[4,5,6],[7,8,9]]
cho=int(input("Enter your choice:"))
a = 0

for i in range(0,len(l)):
    for j in range(0,len(l[i])):
        if(l[i][j] == cho):
            l[i][j] = "x" 
            board(l)



