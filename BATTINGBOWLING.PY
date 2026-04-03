import random

class CricketGame:
    def __init__(self):
        self.player_runs = 0
        self.player_wickets = 0
        self.computer_runs = 0
        self.computer_wickets = 0
        self.overs = 0
        self.max_overs = 2
        self.balls_in_over = 0
    
    def player_bat(self):
        """Player batting against computer bowling"""
        print("\n--- Your Turn to Bat ---")
        while self.overs < self.max_overs and self.player_wickets < 3:
            if self.balls_in_over == 6:
                self.overs += 1
                self.balls_in_over = 0
                print(f"Over {self.overs} completed!")
            if self.overs >= self.max_overs:
                break
            
            self.balls_in_over += 1
            computer_bowl = random.choice(['normal', 'wicket', 'dot', 'four', 'six'])
            
            print(f"\nOver {self.overs}.{self.balls_in_over}")
            print(f"Computer bowled: {computer_bowl}")
            shot = input("Your shot (drive/defend/pull): ").lower()
            
            if computer_bowl == 'wicket':
                if shot != 'defend':
                    print("Wicket! Out!")
                    self.player_wickets += 1
                else:
                    print("Shot defended!")
            elif computer_bowl == 'dot':
                print("Dot ball!")
            elif computer_bowl == 'four':
                if shot in ['drive', 'pull']:
                    self.player_runs += 4
                    print("Four runs!")
                else:
                    print("Single run")
                    self.player_runs += 1
            elif computer_bowl == 'six':
                if shot == 'pull':
                    self.player_runs += 6
                    print("Six runs!")
                else:
                    self.player_runs += 2
                    print("Two runs")
            elif computer_bowl == 'normal':
                self.player_runs += 1
                print("Single run")
        
        print(f"\nYour innings: {self.player_runs} runs, {self.player_wickets} wickets")
    
    def computer_bat(self):
        """Computer batting"""
        print("\n--- Computer's Turn to Bat ---")
        self.overs = 0
        self.balls_in_over = 0
        
        while self.overs < self.max_overs and self.computer_wickets < 3:
            if self.balls_in_over == 6:
                self.overs += 1
                self.balls_in_over = 0
            if self.overs >= self.max_overs:
                break
            
            self.balls_in_over += 1
            runs = random.randint(0, 6)
            self.computer_runs += runs
            print(f"Over {self.overs}.{self.balls_in_over}: Computer scored {runs} runs")
    
    def play(self):
        """Main game loop"""
        print("=== Cricket Batting & Bowling ===")
        self.player_bat()
        self.computer_bat()
        
        print("\n=== Final Score ===")
        print(f"Your Score: {self.player_runs}")
        print(f"Computer Score: {self.computer_runs}")
        
        if self.player_runs > self.computer_runs:
            print("You won!")
        elif self.computer_runs > self.player_runs:
            print("Computer won!")
        else:
            print("It's a tie!")

if __name__ == "__main__":
    game = CricketGame()
    game.play()