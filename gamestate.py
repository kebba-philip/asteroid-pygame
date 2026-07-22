class GameState:
    def __init__(self):
        self.lives = 3

    def lose_life(self):
        self.lives -= 1
        print("Lives remaining:", self.lives)

    def is_game_over(self):
        return self.lives <= 0
