import sqlite3


class Database:
    def __init__(self, database):
        self.db = sqlite3.connect(database)
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()

    def show_movies(self):
        query = """
            SELECT movie_id, movie_name, rating
            FROM Movies
            ORDER BY rating DESC
        """
        return self.cursor.execute(query).fetchall()

    def get_movie(self, movie_id):
        query = """
            SELECT movie_name
            FROM Movies
            WHERE movie_id = ?
        """
        return self.cursor.execute(query, (movie_id, )).fetchone()

    def show_movie_projection(self, movie_id, date=None):
        query = """
            SELECT p.projection_id, date, time, type, 100 - COUNT(row) AS available_spots
            FROM Projections AS p
            LEFT JOIN Reservations AS R
            ON p.projection_id = r.projection_id
            WHERE movie_id = ?
            {}
            GROUP BY type, time, date
            ORDER BY date, time ASC
        """
        if date is not None:
            query = query.format("""
                AND date = ?
            """)
            return self.cursor.execute(query, (movie_id, date)).fetchall()
        else:
            query = query.format('')
            return self.cursor.execute(query, (movie_id,)).fetchall()

    def get_available_spots(self, projection_id):
        query = """
            SELECT row, col
            FROM Reservations
            WHERE projection_id = ?
        """
        row = ['.'] * 10
        hall = [row.copy() for x in range(10)]
        spots = self.cursor.execute(query, (projection_id, )).fetchall()
        for spot in spots:
            hall[spot['row'] - 1][spot['col'] - 1] = 'X'
        return hall

    def make_reservations(self, user_name, projection_id, spots):
        query = """
            INSERT INTO Reservations (username, projection_id, row, col)
            VALUES (?, ?, ?, ?)
        """
        reservations = []
        for spot in spots:
            reservations.append((user_name, projection_id, spot[0], spot[1]))
        self.cursor.executemany(query, reservations)
        # self.db.commit()

    def cancel_reservation(self, user_name):
        query = """
            DELETE FROM Reservations
            WHERE username = ?
        """
        self.cursor.execute(query, (user_name, ))


def main():
    cinema = Database("cinema.db")
    print(cinema.get_movie(1)['movie_name'])
    # print(cinema.check_availability(1, 2, 1))
    # for proj in cinema.show_movie_projection(1, '2014-04-01'):
    #     print("[{}] - {} {} ({}) - {} spots available".format(proj[0], proj[1], proj[2], proj[3], proj[4]))
    cinema.make_reservations('nn', 3, [(2, 1), (2, 2)])
    print(cinema.get_available_spots(3))
    cinema.cancel_reservation('nn')
    print(cinema.get_available_spots(3))

if __name__ == '__main__':
    main()
