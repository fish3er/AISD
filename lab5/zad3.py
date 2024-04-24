import time
def hanoi_it(n, sour, dest, buff):
    moves=0
    i = 1
    while sour or dest:
        if i % 3 == 1:
            if not sour:
                sour.append(dest.pop())
                
            elif not dest:
                dest.append(sour.pop())
                
            elif sour[-1] < dest[-1]:
                dest.append(sour.pop())
                
            else:
                sour.append(dest.pop())
                
        elif i % 3 == 2:
            if not sour:
                sour.append(buff.pop())
                
            elif not buff:
                buff.append(sour.pop())
                
            elif sour[-1] < buff[-1]:
                buff.append(sour.pop())
                
            else:
                sour.append(buff.pop())
                
        else:
            if not buff:
                buff.append(dest.pop())
                
            elif not dest:
                dest.append(buff.pop())
                
            elif buff[-1] < dest[-1]:
                dest.append(buff.pop())
                
            else:
                buff.append(dest.pop())
                
        i += 1
        moves +=1
    return moves
def hanoi_re(n, sour, dest, buff):
    moves = 0
    if n == 1:
        return 1
    hanoi_re(n-1, sour, buff, dest)
    moves += hanoi_re(n-1,sour, dest, buff)
    moves  += 1
    moves += hanoi_re(n-1, buff, dest, sour)
    return moves

def main():
    n = 8 # ilosc dusków

    sourrec = "sour"
    destrec = "dest"
    buffrec = "buff"

    sourit=[]
    destit=[]
    buffit =[]

    for i in range(n):
        sourit.append(i+1)
    sourit.sort(reverse=True)

    start_rec = time.time()
    print("Number of moves in recursive: ", hanoi_re(n,sourrec, destrec, buffrec))
    print("Time needed for recursive: " ,time.time()-start_rec)


    start_it = time.time()
    print("Number of moves in iteration: ", hanoi_it(n,sourit, destit, buffit))
    print("Time needed for iteration: " ,time.time()-start_it)

if __name__ == '__main__':
    main()