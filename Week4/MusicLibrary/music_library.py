import re
import json
import sys
import time
import datetime
from random import choice
from mutagen.easyid3 import EasyID3 as MP3
from mutagen.id3 import ID3, TALB, TLEN
from prettytable import PrettyTable
from settings import PLAYLIST_PATH

class AlredyAdded(Exception):
    pass

class NoSuchSong(Exception):
    pass

class NoMoreSongs(Exception):
    pass

class SongLength:

    def __init__(self, length):
        self.__hours = 0
        self.__minutes = 0
        self.__seconds = 0
        parts = [int(part.strip()) for part in length.split(":")]
        if len(parts) == 3:
            if parts[1] < 60 and parts[2] < 60:
                self.__hours = parts[0]
                self.__minutes = parts[1]
                self.__seconds = parts[2]
            else:
                raise ValueError("Length not proper format: {}".format(length))
        elif len(parts) == 2:
            if parts[0] < 60 and parts[1] < 60:
                self.__minutes = parts[0]
                self.__seconds = parts[1]
            else:
                raise ValueError("Length not proper format: {}".format(length))
        else:
                raise ValueError("Length not proper format: {}".format(length))

    def hours(self):
        return self.__hours

    def minutes(self):
        return self.__hours * 60 + self.__minutes

    def seconds(self):
        return self.__hours * 3600 + self.__minutes * 60 + self.__seconds


class Song:


    def __init__(self, title, artist, album, length):
        self.__title = title
        self.__artist = artist
        self.__album = album
        self.__proper_length = SongLength(length)
        self.__length = length

    def title(self):
        return self.__title

    def artist(self):
        return self.__artist

    def album(self):
        return self.__album

    def length(self):
        return self.__length

    def __str__(self):
        return "{} - {} from {} - {}".format(self.__title, self.__artist, self.__album, self.__length)

    def __repr__(self):
        return "Song('{}', '{}', '{}', '{}')".format(self.__title, self.__artist, self.__album, self.__length)

    def __eq__(self, other):
        eq1 = self.__title == other.__title
        eq2 = self.__artist == other.__artist
        eq3 = self.__album == other.__album
        eq4 = self.__length == other.__length
        return eq1 and eq2 and eq3 and eq4

    def __hash__(self):
        return hash(self.__str__())

    def duration(self, seconds=False, minutes=False, hours=False):
        if seconds:
            return self.__proper_length.seconds()
        if minutes:
            return self.__proper_length.minutes()
        if hours:
            return self.__proper_length.hours()
        else:
            return self.__length


    def prepare_json(self):
        song_dict = self.__dict__
        return {key: song_dict[key] for key in song_dict if not key.startswith("_")}


class Playlist:
    def __init__(self, name="NewPlaylist", repeat=False, shuffle=False):
        self.__name = name
        self.__repeat = repeat
        self.__shuffle = shuffle
        self.playlist = []
        self.__index = 0
        self.__not_played = []
        self.num_of_songs = 0

    def name(self):
        return self.__name

    def __str__(self):
        return "{}".format(self.__name)

    def __repr__(self):
        for_save = [repr(song) for song in self.playlist]
        return json.dumps(for_save, indent=True)

    def change_repeat(self, repeat):
        self.__repeat = repeat

    def change_shuffle(self, shuffle):
        self.__shuffle = shuffle

    def add_song(self, song):
        self.playlist.append(song)
        self.__not_played.append(self.num_of_songs)
        self.num_of_songs += 1

    def remove_song(self, song):
        if song in self.playlist:
            self.playlist.remove(song)
        else:
            raise NoSuchSong

    def add_songs(self, songs):
        self.playlist += songs
        for song in songs:
            self.__not_played.append(self.num_of_songs)
            self.num_of_songs += 1


    def total_length(self):
        duration = sum([song.duration(seconds=True) for song in self.playlist])
        return str(datetime.timedelta(seconds=duration))

    def artists(self):
        histogram = {}
        for song in self.playlist:
            if song in histogram:
                histogram[song.artist()] += 1
            else:
                histogram[song.artist()] = 1
        return histogram

    def shuffle(self):
        if len(self.__not_played) == 0 and self.__repeat == True:
            self.__not_played = [index for index in range(0, len(self.playlist))]
        elif len(self.__not_played) == 0:
            raise NoMoreSongs

        index = choice(self.__not_played)
        self.__not_played.remove(index)
        return self.playlist[index]

    def __next_song(self):
        song = self.playlist[self.__index]
        self.__index += 1
        return song


    def next_song(self):
        if self.__repeat == True and self.__shuffle == False:
            if self.__index == len(self.playlist):
                self.__index = 0
            return self.__next_song()
        elif self.__shuffle == True:
            return self.shuffle()
        else:
            if self.__index == len(self.playlist):
                raise NoMoreSongs
            return self.__next_song()

    def pprint_playlist(self):
        table = PrettyTable(["Artist", "Song", "Length"])
        for song in self.playlist:
            table.add_row([song.artist(), song.title(), song.length()])
        print(table)

    def save(self):
        filename = ""
        for char in self.__name:
            if char == " ":
                char = "-"
            filename += char

        with open("{}{}.json".format(PLAYLIST_PATH, filename), 'w') as f:
            f.write(self.__repr__())

    @staticmethod
    def load(filename):
        name = ""
        for char in filename:
            if char == "-":
                char = " "
            if char == ".":
                break
            name += char
        playlist = Playlist(name)

        with open("{}{}".format(PLAYLIST_PATH, filename), 'r') as f:
            contents = f.read()
            json_playlist = json.loads(contents)
            for song in json_playlist:
                new_song = eval(song)
                playlist.add_song(new_song)
            return playlist

#def main():
#    my_song = Song("Solder Of Frortune", "Deep Purple", "Stormbringer", "3:14")
#    second_song = Song("I Stand Alone", "Godsmack", "Awake", "4:30")
#    bard = Song("The Bards Song", "Blind Guardian", "Somwhere Far Beyond", "3:28")
#    rock = Playlist("Rock songs", repeat=True)
#    rock.add_songs([my_song, second_song, bard])
#    rock.pprint_playlist()
#    rock.save()
#    rock = Playlist.load("Rock-songs.json")
#    print(rock.name())
#    for song in rock.playlist:
#        print(song)

if __name__ == '__main__':
    main()

