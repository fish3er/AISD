def hanoi(n, sour, dest, buff):
    moves=0
    i = 1
    while sour or dest:
        if i % 3 == 1:
            if not sour:
                sour.append(dest.pop())
                print("from dest to sour")
            elif not dest:
                dest.append(sour.pop())
                print("from sour to dest")
            elif sour[-1] < dest[-1]:
                dest.append(sour.pop())
                print('from sour to dest')
            else:
                sour.append(dest.pop())
                print("from dest to sour")
        elif i % 3 == 2:
            if not sour:
                sour.append(buff.pop())
                print("from buff to sour")
            elif not buff:
                buff.append(sour.pop())
                print("from sour to buff")
            elif sour[-1] < buff[-1]:
                buff.append(sour.pop())
                print("from sour to buff")
            else:
                sour.append(buff.pop())
                print("from buff to sour")
        elif i%3 ==0:
            if not buff:
                buff.append(dest.pop())
                print("from dest to buff")
            if not dest:
                dest.append(buff.pop())
                print("from buff to dest")
            elif buff[-1] < dest[-1]:
                dest.append(buff.pop())
                print("from buff to dest")
            else:
                buff.append(dest.pop())
                print("from dest to buff")
        i += 1
        moves +=1
    print(moves)

def main():
    source = []
    destination = []
    auxiliary = []
    n= 10 # liczba dysków
    for i in range(n):
        source.append(n-i)
    hanoi(n, source, destination,auxiliary )
if __name__ == '__main__':
    main()
