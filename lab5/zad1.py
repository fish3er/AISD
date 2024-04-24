def hanoi(n, sour, dest, buff):
    moves = 0
    if n == 1:
        print(f"Przenieś krążek {n} z {sour} do {dest}")
        return 1
    hanoi(n-1, sour, buff, dest)
    moves += hanoi(n-1,sour, dest, buff)
    print(f"Przenieś krążek {n} z {sour} do {dest}")
    moves  += 1
    moves += hanoi(n-1, buff, dest, sour)
    return moves
def main():
    n = 10  
    source = "Igła startowa"
    destination = "Igła docelowa"
    auxiliary = "Igła pomocnicza"
    hanoi(n, source, destination, auxiliary)
    print(hanoi(n, source, destination, auxiliary))
if __name__ == '__main__':
    main()