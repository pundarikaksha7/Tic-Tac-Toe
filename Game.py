def cls(): print("\n"*100)
def layout(board):
    cls()
    print(board[0]+"|",board[1]+"|",board[2])
    print(board[3]+"|",board[4]+"|",board[5])
    print(board[6]+"|",board[7]+"|",board[8])


def chances():
        win=False
        for i in range(0,9):
            if i%2==0:
                    #p1 gets to choose a position if i is even 
                    turn=int(input("ENTER THE POSITION WHERE YOU WANT {}".format(p1)))
                    board[turn]=p1
                    layout(board)
                    if board[0]==board[1] and board[0]==board[2]:
                        win=True

                    elif board[0]==board[4] and board[0]==board[8]:
                        win=True

                    elif board[1]==board[4] and board[1]==board[7]:
                        win=True

                    elif board[2]==board[4] and board[2]==board[6]:
                        win=True

                    elif board[3]==board[4] and board[3]==board[5]:
                        win=True

                    elif board[0]==board[3] and board[0]==board[6]:
                        win=True

                    elif board[2]==board[5] and board[2]==board[8]:
                        win=True
        
                    elif board[6]==board[7] and board[6]==board[8]:
                        win=True
                    else:
                        pass
                    if win==True:
                        print("PLAYER 1 WINS!")
                        playagain=""
                        while playagain!="Y" or playagain!="N":
                            playagain=input("WANT TO PLAY AGAIN? PRESS Y FOR YES OR N FOR NO")
                            if playagain in ["y","n","Y","N"]:
                                playagain=playagain.upper()
                                break
                            else:
                                print("PLEASE PRESS ONLY Y OR N")
                        print("PLAYERS CHOOSE TO PLAYAGAIN? ")
                        return playagain
                        break
                    elif win==False and i==8:
                        print("ITS A DRAW!")
                        playagain=""
                        while playagain!="Y" or playagain!="N":
                            playagain=input("WANT TO PLAY AGAIN? PRESS Y FOR YES OR N FOR NO")
                            if playagain in ["y","n","Y","N"]:
                                playagain=playagain.upper()
                                break
                            else:
                                print("PLEASE PRESS ONLY Y OR N")
                        print("PLAYERS CHOOSE TO PLAYAGAIN? ")
                        return playagain

            else:
                    #p2 gets to choose now
                    turn=int(input("ENTER THE POSITION WHERE YOU WANT {} ".format(p2)))
                    board[turn]=p2
                    layout(board)
                    if board[0]==board[1] and board[0]==board[2]:
                        win=True

                    elif board[0]==board[4] and board[0]==board[8]:
                        win=True

                    elif board[1]==board[4] and board[1]==board[7]:
                        win=True

                    elif board[2]==board[4] and board[2]==board[6]:
                        win=True

                    elif board[3]==board[4] and board[3]==board[5]:
                        win=True

                    elif board[0]==board[3] and board[0]==board[6]:
                        win=True

                    elif board[2]==board[5] and board[2]==board[8]:
                        win=True

                    elif board[6]==board[7] and board[6]==board[8]:
                        win=True
                    else:
                        pass
                    if win==True:
                        print("PLAYER 2 WINS!")
                        playagain=""
                        while playagain!="Y" or playagain!="N":
                            playagain=input("WANT TO PLAY AGAIN? PRESS Y FOR YES OR N FOR NO")
                            if playagain in ["y","n","Y","N"]:
                                playagain=playagain.upper()
                                break
                            else:
                                print("PLEASE PRESS ONLY Y OR N")
                        print("PLAYERS CHOOSE TO PLAYAGAIN? ")
                        return playagain
                        break
                    elif win==False and i==8:
                        print("ITS A DRAW!")
                        playagain=""
                        while playagain!="Y" or playagain!="N":
                            playagain=input("WANT TO PLAY AGAIN? PRESS Y FOR YES OR N FOR NO")
                            if playagain in ["y","n","Y","N"]:
                                playagain=playagain.upper()
                                break
                            else:
                                print("PLEASE PRESS ONLY Y OR N")
                        print("PLAYERS CHOOSE TO PLAYAGAIN? ")
                        return playagain

board=["0","1","2","3","4","5","6","7","8"]
print("HERES YOUR BOARD")
print(board[0]+"|",board[1]+"|",board[2])
print(board[3]+"|",board[4]+"|",board[5])
print(board[6]+"|",board[7]+"|",board[8])
print("NOW LETS CHOOSE THE MARKERS")
p2=""
p1=""
while p1!='X' or p1!="O":
    p1=input("PLAYER ONE CHOOSE X OR O:")
    if p1 in ["x","o","X","O"]:
        p1=p1.upper()
        break
    else:
         pass
if p1=="X":
    p2="O"
else:
     p2="X"
print("P1 CHOOSES "+p1, "P2 CHOOSES "+p2)
print(" HOW TO PLAY ")
print(" CHOOSE THE INDEX WHERE YOU WANT YOUR MARKER THEN CHOOSE THE MARKER TURN WISE")
print("LET THE GAME BEGIN ")
chances()

