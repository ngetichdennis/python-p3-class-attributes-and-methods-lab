class Song:
    # Initialize class-level attributes
    count = 0
    genre_count = {}
    artist_count = {}
    genres = set()
    artists = set()

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class-level attributes
        Song.count += 1
        Song.genres.add(genre)
        Song.artists.add(artist)

        # Update genre count
        Song.genre_count.setdefault(genre, 0)
        Song.genre_count[genre] += 1

        # Update artist count
        Song.artist_count.setdefault(artist, 0)
        Song.artist_count[artist] += 1

    @classmethod
    def create_song(cls, name, artist, genre):
        """
        Create a new Song instance and update class-level attributes.
        """
        return cls(name, artist, genre)

# Test data
Song.create_song("99 Problems", "Jay Z", "Rap")
Song.create_song("Halo", "Beyonce", "Pop")
Song.create_song("Smells Like Teen Spirit", "Nirvana", "Rock")



