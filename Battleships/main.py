from Strategy import *
from Player import *
from Tournament import *

playTournament = True

if playTournament:
    players = [
        Player(Randomized()),
        Player(TopLeft()),
        Player(MiddleOut()),
        Player(RandomThenSink())
    ]

    tournament = Tournament(players, rounds=1_000)
    tournament.begin()
    tournament.print_score()
    tournament.graph(tournament.data)

else:

    player1 = Player(TopLeft())
    player2 = Player(MiddleOut())

    while not player1.hasWon(against=player2) and not player2.hasWon(against=player1):
        player1.attack(player2)
        player2.attack(player1)

    player1.visualise()
    player2.visualise()

    print("P1", player1.score)
    print("P2", player2.score)
    print("Draw" if player1.hasWon(against=player2) and player2.hasWon(against=player1) else
          "Player1" if player1.hasWon(against=player2) else
          "Player2", "has won the game")
