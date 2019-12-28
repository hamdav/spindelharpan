from QPlayer import QPlayer
from SpindelTable import Table



# Run 100 games 
wonGames = 0
N = 1
qPlayer = QPlayer(None)

for i in range(N):
    print("Game: " + str(i))

    table = Table(1)
    qPlayer.newTable(table)
    lastPile = False

    # Game loop
    while True:

        # distribute loop
        n = 0
        while True:

            # Prevent going back and forth
            n += 1
            if n > 1000 and not lastPile:
                pass
                #break

            # Print every something
            if not n % 2000:
                print(n)

            possMoves = table.possibleMoves()
            if not possMoves:
                break

            #breakpoint()
            qPlayer.move()

        if table.piles:
            table.distribute()
            print("Distributing")
            if not table.piles:
                lastPile = True
            continue

        break

    if table.isWon():
        wonGames += 1
        print("WON")
    else:
        print("lost")

print(f"Number of won games: {wonGames} out of {N}")




