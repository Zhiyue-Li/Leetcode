from collections import defaultdict
def favoriteGenres(userSongs, songGenres):
    song_to_genre = {}
    for genre, songs in songGenres.items():
        for song in songs:
            song_to_genre[song] = genre

    for user, songs in userSongs.items():
        counter = defaultdict(int)
        for song in songs:
            if song in song_to_genre:
                counter[song_to_genre[song]] += 1
        maxCount = max(counter.values()) if counter else 0
        res = [g for g in counter.keys() if counter[g] == maxCount]
        userSongs[user] = res
    return userSongs

arg1 = {  
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
}
arg2 = {
}

print(favoriteGenres(arg1, arg2))