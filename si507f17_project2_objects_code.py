# coding = utf-8
# SI 507 F17 Project 2 - Objects
import requests
import json
import unittest

print("\n*** *** PROJECT 2 *** ***\n")


def params_unique_combination(baseurl, params_d, private_keys=["api_key"]):
    alphabetized_keys = sorted(params_d.keys())
    res = []
    for k in alphabetized_keys:
        if k not in private_keys:
            res.append("{}-{}".format(k, params_d[k]))
    return baseurl + "_".join(res)


def sample_get_cache_itunes_data(search_term, media_term="all"):
    CACHE_FNAME = 'cache_file_name.json'
    try:
        cache_file = open(CACHE_FNAME, 'r')
        cache_contents = cache_file.read()
        CACHE_DICTION = json.loads(cache_contents)
        cache_file.close()
    except:
        CACHE_DICTION = {}
    baseurl = "https://itunes.apple.com/search"
    params = {}
    params["media"] = media_term
    params["term"] = search_term
    unique_ident = params_unique_combination(baseurl, params)
    if unique_ident in CACHE_DICTION:
        return CACHE_DICTION[unique_ident]
    else:
        CACHE_DICTION[unique_ident] = json.loads(requests.get(baseurl, params=params).text)
        full_text = json.dumps(CACHE_DICTION)
        cache_file_ref = open(CACHE_FNAME, "w")
        cache_file_ref.write(full_text)
        cache_file_ref.close()
        return CACHE_DICTION[unique_ident]


#[PROBLEM 1] [250 POINTS]
print("\n***** PROBLEM 1 *****\n")


class Media:
    def __init__(self, media):
        self.title = media.get('trackName')
        self.author = media.get('artistName')
        self.itunes_URL = media.get('trackViewUrl')
        self.itunes_id = media.get('trackId')
        self.seconds = int(media.get('trackTimeMillis', 0) / 1000)

    def __str__(self):
        return "{} by {}".format(self.title, self.author)

    def __repr__(self):
        return "ITUNES MEDIA: {}".format(self.itunes_id)

    def __len__(self):
        return 0

    def __contains__(self, item):
        return item in self.title


#[PROBLEM 2] [400 POINTS]
print("\n***** PROBLEM 2 *****\n")


class Song(Media):
    def __init__(self, song):
        self.title = song.get('trackName')
        self.author = song.get('artistName')
        self.itunes_URL = song.get('trackViewUrl')
        self.itunes_id = song.get('trackId')
        self.album = song.get('collectionName')
        self.track_number = song.get('trackNumber')
        self.genre = song.get('primaryGenreName')
        self.seconds = int(song.get('trackTimeMillis', 0) / 1000)

    def __len__(self):
        return self.seconds


class Movie(Media):
    def __init__(self, movie):
        self.title = movie.get('trackName')
        self.author = movie.get('artistName')
        self.itunes_URL = movie.get('trackViewUrl')
        self.itunes_id = movie.get('trackId')
        self.rating = movie.get('contentAdvisoryRating')
        self.genre = movie.get('primaryGenreName')
        self.description = movie.get('longDescription').encode('utf-8')
        self.mins = int(movie.get('trackTimeMillis', 0) / (1000 * 60))
        self.seconds = self.mins * 60

    def __len__(self):
        return self.mins

    def title_words_num(self):
        if not self.description:
            return 0
        else:
            return len(self.description.split())


#[PROBLEM 3] [150 POINTS]
print("\n***** PROBLEM 3 *****\n")


media_samples = sample_get_cache_itunes_data("love")["results"]

song_samples = sample_get_cache_itunes_data("love", "music")["results"]

movie_samples = sample_get_cache_itunes_data("love", "movie")["results"]


media_list = []
for media in media_samples:
    media_list.append(Media(media))

song_list = []
for song in song_samples:
    song_list.append(Song(song))

movie_list = []
for movie in movie_samples:
    movie_list.append(Movie(movie))

#[PROBLEM 4] [200 POINTS]
print("\n***** PROBLEM 4 *****\n")


def writeToCSVFile(fileName, media_list):
    with open(fileName, 'w') as writer:
        writer.write("title, artist, id, url, length\n")
        for media in media_list:
            writer.write(
                "{}", {}, {}, {}, {}\n'.format(media.title, media.author,
                                      media.itunes_id, media.itunes_URL, len(media)))

writeToCSVFile("movies.csv", movie_list)
writeToCSVFile("songs.csv", song_list)
writeToCSVFile("media.csv", media_list)
