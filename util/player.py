from base import Player

player = Player("Roland")

player.connect()
while True:
    player.take_turn(input('Player:'))
