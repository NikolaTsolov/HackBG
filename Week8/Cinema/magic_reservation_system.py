from database import Database
import sys

class CLI:
    def __init__(self):
        self.cinema = Database("cinema.db")
        self.username = ""
        self.tickets = 0
        self.options = {}
        self.available = {}

    STEPS = [
        "STEP 1",
        "STEP 2",
        "STEP 3",
        "STEP 3"
    ]

    def step_one(self):
        self.username = input("Choose name>")
        self.tickets = input("Choose number of tickets>")
        self.show_movies()

    def step_two(self):
        movie = input("Choose a movie>")
        self.show_movie_projections(movie)

    def step_three(self):
        while False:
            projection = input("Choose a projection>")
            if self.available[projection] > self.tickets:
                break
        self.cinema.get_available_spots(projection)

    def step_four(self):
        pass




    def show_movies(self):
        print("Current movies:")
        for movie in self.cinema.show_movies():
            print("[{}] - {} ({})".format(movie[0], movie[1], movie[2]))


    def show_movie_projections(self, movie_id, date=None):
        print("Projections for movie '{}':".format())
        if date is not None:
            for proj in self.cinema.show_movie_projection(movie_id, date):
                self.available[proj[0]] = proj[4]
                massage = "[{}] - {} ({}) - {} spots available"
                print(massage.format(proj[0], proj[2], proj[3], proj[4]))
        else:
            for proj in self.cinema.show_movie_projection(movie_id):
                self.available[proj[0]] = proj[4]
                massage = "[{}] - {} {} ({}) - {} spots available"
                print(massage.format(proj[0], proj[1], proj[2], proj[3], proj[4]))




    def make_reservation(self):
        self.step_one()
        self.step_two()
        self.step_three()


def main():
    i_o = CLI()
    i_o.make_reservation()


if __name__ == '__main__':
    main()

