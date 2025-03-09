import tkinter as tk
import random

class PacmanGame:
    def __init__(self):
        self.HISCORE_FILENAME = "hiscore.txt"

        # Create window
        self.window = tk.Tk()
        self.window.title("Pac-Man Game")

        # Setup Canvas
        self.canvas = tk.Canvas(self.window, width=400, height=400, bg="black")
        self.canvas.pack()

        # List of wall frames
        self.walls = [
            (50, 50, 350, 70),  # Top Wall
            (50, 50, 70, 350),  # Left Wall
            (330, 50, 350, 350),  # Right Wall
            (50, 330, 350, 350)  # Bottom Wall
        ]

        self.game_over = False
        self.score = 0
        self.hiscore = self.load_score()

        self.ghost_movement_timeout = 500
        self.ghost_movement = 5

        # Draw maze
        self.draw_maze()
        self.create_food(25)

        # setup pacman and ghost
        self.pacman = self.canvas.create_oval(90, 90, 110, 110, fill="yellow", outline="yellow")
        self.ghosts = []
        self.create_ghosts(3)

        self.score_text = self.canvas.create_text(310, 25, text=str(self.score), fill="white", font=("Arial", 24))
        self.hiscore_text = self.canvas.create_text(110, 25, text=str(self.hiscore), fill="white", font=("Arial", 24))
        self.game_over_text = self.canvas.create_text(200, 200, text="", fill="white", font=("Arial", 24))

        # start timers
        self.move_ghost()
        self.update_score()

        # setup controls
        self.window.bind("<Up>", self.move_pacman)
        self.window.bind("<Down>", self.move_pacman)
        self.window.bind("<Left>", self.move_pacman)
        self.window.bind("<Right>", self.move_pacman)

        self.window.focus_force()
        self.window.mainloop()
    #enddef

    def save_score(self):
        """
        Saves current score as the highest
        """
        file = open(self.HISCORE_FILENAME, "w")
        file.write(f"{self.score}")
        file.close()
    #enddef

    def load_score(self):
        """
        Loads previously saved score
        :return: Integer, 0 when there is no score
        """

        file = open(self.HISCORE_FILENAME, "r")
        try:
            score = file.readline()
        except:
            self.score = ""
        #endtry
        file.close()

        if len(score) == 0:
            return 0
        #endif

        return int(score)
    #enddef

    def create_ghosts(self, num):
        """
        Creates ghosts and puts them in list
        :param num: Number of ghosts
        """
        colors = ["red", "white", "pink", "cyan", "purple"]
        random.shuffle(colors)

        # Find a unique color for each ghost
        # make a list of colors you have seen / used
        used_colors = []

        size = 20
        for i in range(num):
            ghost_pos = random.randint(180, 250)

            new_color = None

            new_color = random.choice(colors)

            if num < len(colors):
                while new_color in used_colors:
                    random.shuffle(colors)
                    new_color = random.choice(colors)
                # endwhile
            # endif

            used_colors.append(new_color)

            ghost = self.canvas.create_oval(ghost_pos, ghost_pos, ghost_pos+size, ghost_pos+size, fill=new_color, outline=new_color)
            self.ghosts.append(ghost)
        #endfor
    #enddef


    def draw_maze(self):
        # a single wall is: x, y, width, height
        for wall in self.walls:
            self.canvas.create_rectangle(wall, fill="blue", outline="blue")
        #endfor
    #enddef

    def move_pacman(self, event):
        direction = {
            "Up": (0, -10),
            "Down": (0, 10),
            "Left": (-10, 0),
            "Right": (10, 0)
        }
        dx, dy = direction[event.keysym]
        if self.can_move(self.pacman, dx, dy):
            self.canvas.move(self.pacman, dx, dy)
        #endif

        self.check_collision_with_food()
    #enddef

    def move_ghost(self):
        vectors = [
            (0, -self.ghost_movement),
            (0, self.ghost_movement),
            (-self.ghost_movement, 0),
            (self.ghost_movement, 0)
        ]

        for ghost in self.ghosts:
            dx, dy = random.choice(vectors)

            if self.can_move(ghost, dx, dy):
                self.canvas.move(ghost, dx, dy)
            #endif

            self.check_collision_with_ghost()

            if self.game_over:
                return
            #endif
        #endfor

        # Uses timer to call function repeatedly so it can randomly keep moving the ghost
        self.window.after(self.ghost_movement_timeout, self.move_ghost)

        # Makes the ghosts move longer distances
        self.ghost_movement += 1
        if self.ghost_movement > 25:
            self.ghost_movement = 25
        #endif

        self.ghost_movement_timeout -= 25

        if self.ghost_movement_timeout <= 150:
            self.ghost_movement_timeout = 150
        #endif
    #enddef

    def create_food(self, num):
        """
        Creates food for pacman and adds it to the canvas
        """
        self.food = []
        for _ in range(num):
            x, y = random.randint(100, 300), random.randint(100, 300)
            food_item = self.canvas.create_oval(x, y, x + 10, y + 10, fill="gold", outline="gold")
            self.food.append(food_item)
        #endfor
    #enddef

    def check_collision_with_food(self):
        pacman_coords = self.canvas.coords(self.pacman)
        for food_item in self.food:
            if self.canvas.bbox(food_item) and self.overlap(pacman_coords, self.canvas.coords(food_item)):
                self.canvas.delete(food_item)
                self.food.remove(food_item)

                self.score += 1
            #endif
        #endfor

        if not self.food:
            self.display_game_over("WINNER!")
        #endif

        self.check_collision_with_ghost()
        self.update_score()

    #enddef

    def overlap(self, coords1, coords2):
        return not (coords1[2] < coords2[0] or coords1[0] > coords2[2] or coords1[3] < coords2[1] or coords1[1] >
                    coords2[3])
    #enddef

    def can_move(self, item, dx, dy):
        """
        Checks if the shape can move after applying the delta x and y
        :param item: shape
        :param dx: horizontal movement
        :param dy: vertical movement
        :return: boolean
        """

        # Nothing should move when the game is over
        if self.game_over:
            return False
        #endif

        # Returns top left and top right coordinates of the item / shape
        future_coords = self.canvas.coords(item)

        # Create a "future" coordinate where the item will be after
        # it's moved
        future_coords = (
            future_coords[0] + dx,
            future_coords[1] + dy,

            future_coords[2] + dx,
            future_coords[3] + dy
        )

        # Check if the future coordinates are within the walls
        left_wall = self.walls[1][2]
        right_wall = self.walls[2][0]
        top_wall = self.walls[0][3]
        bottom_wall = self.walls[3][1]

        return (left_wall <= future_coords[0] <= right_wall - (future_coords[2] - future_coords[0]) and
                top_wall <= future_coords[1] <= bottom_wall - (future_coords[3] - future_coords[1]))
    #enddef

    def check_collision_with_ghost(self):
        for ghost in self.ghosts:
            if not self.game_over:
                pacman_coords = self.canvas.coords(self.pacman)
                ghost_coords = self.canvas.coords(ghost)

                if self.overlap(pacman_coords, ghost_coords):
                    self.display_game_over("GAME OVER")
                #endif
            #endif
        #endfor
    #enddef

    def display_game_over(self, message):
        self.game_over = True
        self.canvas.itemconfigure(self.game_over_text, text=message)

        self.colorize_game_over()

        if self.hiscore < self.score:
            self.save_score()
        #endif
    #enddef

    def colorize_game_over(self):
        colours = ["red", "orange", "yellow", "green", "blue", "pink"]
        colour = random.choice(colours)
        self.canvas.itemconfigure(self.game_over_text, fill=colour)
        self.window.after(250, self.colorize_game_over)
    #enddef

    def update_score(self):
        final_score = f"Score: {self.score}"
        self.canvas.itemconfigure(self.score_text, text=final_score)

        final_hiscore = f"Hi-Score: {self.hiscore}"
        self.canvas.itemconfigure(self.hiscore_text, text=final_hiscore)
    #enddef
#endclass

# This is a single window game, so the class will
# create it for us
PacmanGame()

