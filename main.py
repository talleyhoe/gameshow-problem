# Assign prizes
# Pick door
# Choose to Switch
# Log Result

from random import randint, randrange
from tqdm import tqdm

SIMULATED_GAMES = 1_000_000

class Show:
    doors: bool = [0, 0, 0]
    door_picked = 0    # Integer less than or equal to 3
    door_revealed = 0  # Integer less than or equal to 3 
    door_remaining = 0 # Integer less than or equal to 3 
    door_switched: bool = 0
    prize_found: bool = 0

    def reset(self):
        self.doors = [0, 0, 0]
        self.door_picked = 0   
        self.door_revealed = 0
        self.door_remaining = 0
        self.door_switched: bool = 0
        self.prize_found: bool = 0

    def assign_prize(self):
        prize_door = randrange(3)
        self.doors[prize_door] = 1

    def pick_door(self):
        self.door_picked = randint(1, 3)

    # Oh no! The logic is wrong. We must reveal neither the door with a prize 
    #   nor the door we picked. So this is not random unless we pick correctly
    def reveal_door(self):
        if (self.door_picked == 0):
            raise ValueError("You must pick a door before revealing")
        bad_doors = [1, 2, 3]
        del bad_doors[self.door_picked - 1]
        if self.doors[bad_doors[0] - 1]:
            self.door_revealed  = bad_doors[1]
            self.door_remaining = bad_doors[0]
        else:
            self.door_revealed  = bad_doors[0]
            self.door_remaining = bad_doors[1]

    def decide_switch(self):
        switched: bool = randrange(2)
        self.door_switched = switched
        if switched:
            self.door_picked = self.door_remaining

    def open_doors(self):
        self.prize_found = self.doors[self.door_picked - 1]

    def play_game(self):
        self.reset()
        self.assign_prize()
        self.pick_door()
        self.reveal_door()
        self.decide_switch()
        self.open_doors()


def main():
    games_played = 0
    games_won = 0
    games_switched = 0
    games_won_and_switched = 0
    game_show = Show()
    for game in tqdm(range(SIMULATED_GAMES)):
        game_show.play_game()
        games_played += 1
        games_won += game_show.prize_found
        games_switched += game_show.door_switched
        games_won_and_switched += (game_show.prize_found & game_show.door_switched)

    print("games won: {}".format(games_won/games_played))
    print("games switched: {}".format(games_switched/games_played))
    print("games_switched_and_won: {}"
           .format(games_won_and_switched/games_switched))
        

if __name__ == "__main__":
    main()
