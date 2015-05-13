import re
from random import randint, shuffle
from prettytable import PrettyTable
import json
import sys
import time
import datetime

class AlredyAdded(Exception):
    pass

class NoSuchSong(Exception):
    pass

class NoMoreSongs(Exception):
    pass

class SongLength:
    def __init__(self, length):
        self.length = length
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        parts = [int(part.strip()) for part in length.split(":")]

        if len(parts) == 3:
            if parts[1] < 61 and parts[2]:
                self.hours = parts[0]
                self.minutes = parts[1]
                self.seconds = parts[2]
        elif len(parts) == 2:
            self.minutes = parts[0]
            self.seconds = parts[1]
        else:
            raise ValueError("Length not proper format: {}".format(length))

    def get_hours(self):
        return self.hours

    def get_minutes(self):
        return self.hours * 60 + self.minutes

    def get_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


class Song:


    def __init__(self, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length
        self.__length = SongLength(length)

    def __str__(self):
        return "{} - {} from {} - {}".format(self.title, self.artist, self.album, self.length)

    def __eq__(self, other):
        eq1 = self.title == other.title
        eq2 = self.artist == other.artist
        eq3 = self.album == other.album
        eq4 = self.length == other.length
        return eq1 and eq2 and eq3 and eq4

    def __hash__(self):
        return hash(self.__str__())

    def get_length(self, seconds=False, minutes=False, hours=False):
        if seconds:
            return self.__length.get_seconds()
        if minutes:
            return self.__length.get_minutes()
        if hours:
            return self.__length.get_hours()
        else:
            return self.__length()


    def prepare_json(self):
        song_dict = self.__dict__
        return {key: song_dict[key] for key in song_dict if not key.startswith("_")}


class Playlist:
    def __init__(self, name="NewPlaylist", repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.playlist = []
        self.index = 0
        self.list_chek = []

    def __str__(self):
        return "{}".format(self.name)

    def __repr__(self):
        return "Playlist('{}')".format(self.name)

    def add_song(self, song):
        self.playlist.append(song)

    def remove_song(self, song):
        if song in self.playlist:
            self.playlist.remove(song)
        else:
            raise NoSuchSong

    def add_songs(self, songs):
        self.playlist += songs

    def total_length(self):
        duration = sum([song.get_length(seconds=True) for song in self.playlist])
        return str(datetime.timedelta(seconds=duration))

    def artists(self):
        histogram = {}
        for song in self.playlist:
            histogram[song.artist] = 0
        for song in self.playlist:
            histogram[song.artist] += 1
        return histogram


    def next_song(self):
        if self.repeat == True:
            if self.index == len(self.playlist):
                self.index = 0
            song = self.playlist[self.index]
            self.index += 1
            return song
        if self.repeat != True and self.shuffle != True:
            song = self.playlist[self.index]
            if self.index == len(self.playlist)-1:
                raise NoMoreSongs
            self.index += 1

        if self.shuffle == True:
            index = randint(0, len(self.playlist)-1)
            if len(self.list_chek) == 0:
                self.list_chek.append(self.playlist[index])
                return self.playlist[index]
            while True:
                if self.playlist[index] not in self.list_chek:
                    self.list_chek.append(self.playlist[index])
                    return self.playlist[index]
                if len(self.list_chek) == len(self.playlist):
                    self.list_chek =[]
                    self.list_chek.append(self.playlist[index])
                    return self.playlist[index]
                index = randint(0, len(self.playlist)-1)

    def pprint_playlist(self):
        table = PrettyTable(["Artist", "Song", "Length"])
        for song in self.playlist:
            table.add_row([song.artist, song.title, song.length])
        print(table)


    def prepare_json(self):
        data = {
            "name": self.name,
            "songs": [song.prepare_json() for song in self.playlist]
        }

    def save(self, indent=True):
        filename = self.name
        if " " in filename:
            for item in filename:
                if item == " ":
                    item = "-"

        with open("{}.json".format(filename), 'w') as f:
            f.write(json.dumps(self.prepare_json(), indent=indent))

    @staticmethod
    def load(filename):
        with open(filename, 'r') as f:
            contents = f.read()
            data = json.loads(contents)
            p = Playlist(data["name"])
            for dict_data in data["songs"]:
                song = Song(title=dict_data["title"], artist=dict_data["artist"], album=dict_data["album"], length=dict_data["length"])
                p.add_song(song)
            return p



'''randint(0, 1000)'''


def main():
    SoldierOfFortune = Song("Solder Of Frortune", "Deep Purple", "SolderOfFrortune", "3:14")
    IStandAlone = Song("I Stand Alone", "Godsmack", "Awake", "4:30")
    BardSong = Song("Bard'Song", "Follow The Blind", "Blind Guardian", "3:35")
    print(str(SoldierOfFortune))
    in_seconds = SoldierOfFortune.get_length(seconds=True)
    in_seconds2 = IStandAlone.get_length(seconds=True)
    print(in_seconds, in_seconds2)
    rock = Playlist('Rock')
    rock.add_song(BardSong)
    rock.add_song(SoldierOfFortune)
    rock.add_song(IStandAlone)
    print(rock.total_length())
    print(rock.total_length())
    print(rock.artists())
    print(rock.next_song())
    print(rock.next_song())
    rock.pprint_playlist()

    rock.save()
    new_playlist = Playlist.load("Rock.json")
    print(new_playlist.name == "Rock")

if __name__ == '__main__':
    main()

