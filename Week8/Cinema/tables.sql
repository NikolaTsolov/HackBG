DROP TABLE IF EXISTS Movies;
DROP TABLE IF EXISTS Projections;
DROP TABLE IF EXISTS Reservations;
pragma foreign_keys = on;


CREATE TABLE Movies(
  movie_id INTEGER PRIMARY KEY,
  movie_name TEXT,
  rating INTEGER
);

CREATE TABLE Projections(
  projection_id INTEGER PRIMARY KEY,
  movie_id INTEGER,
  type TEXT,
  date DATE,
  time TEXT,
  FOREIGN KEY(movie_id) REFERENCES Movies(movie_id)
);

CREATE TABLE Reservations(
  reservation_id INTEGER PRIMARY KEY,
  username TEXT,
  projection_id INTEGER,
  row INTEGER,
  col INTEGER,
  FOREIGN KEY(projection_id) REFERENCES Projections(projection_id)
);

INSERT INTO Movies(movie_name, rating) VALUES("The Hunger Games: Catching Fire", 7.9);
INSERT INTO Movies(movie_name, rating) VALUES("Wreck-It Ralph", 7.8);
INSERT INTO Movies(movie_name, rating) VALUES("Her", 8.3);

INSERT INTO Projections(movie_id, type, date, time) VALUES(1, "3D", "2014-04-01", "19:10");
INSERT INTO Projections(movie_id, type, date, time) VALUES(1, "2D", "2014-04-01", "19:00");
INSERT INTO Projections(movie_id, type, date, time) VALUES(1, "4DX", "2014-04-02", "21:00");
INSERT INTO Projections(movie_id, type, date, time) VALUES(3, "2D", "2014-04-05", "20:20");
INSERT INTO Projections(movie_id, type, date, time) VALUES(2, "3D", "2014-04-02", "22:00");
INSERT INTO Projections(movie_id, type, date, time) VALUES(2, "2D", "2014-04-02", "19:30");

INSERT INTO Reservations(username, projection_id, row, col) VALUES("RadoRado", 1, 2, 1);
INSERT INTO Reservations(username, projection_id, row, col) VALUES("RadoRado", 1, 3, 5);
INSERT INTO Reservations(username, projection_id, row, col) VALUES("RadoRado", 1, 7, 8);
INSERT INTO Reservations(username, projection_id, row, col) VALUES("Ivo", 3, 1, 1);
INSERT INTO Reservations(username, projection_id, row, col) VALUES("Ivo", 3, 1, 2);
INSERT INTO Reservations(username, projection_id, row, col) VALUES("Mysterious", 5, 2, 3);
INSERT INTO Reservations(username, projection_id, row, col) VALUES("Mysterious", 5, 2, 4);
