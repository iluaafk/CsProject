from Song import Song
from Spotify import Spotify


def main():
    spotify_app = Spotify()
    spotify_app.add_user("Enxhi2803")
    spotify_app.create_playlist_for_user("Enxhi2803", "Favourite Songs")
    spotify_app.create_playlist_for_user("Enxhi2803", "Kot")

    spotify_app.delete_playlist_for_user("Enxhi2803", "Kot")

    test_song= Song("Lol", "lol", "12")
    spotify_app.add_song_to_user_playlist("Enxhi2803", "Kot", test_song)



    first_song = Song("Ne erresiren e  nates", "Andi Shkoza", "5:00")
    second_song = Song("100%", "Gjyste Vulaj", "3:25")

    spotify_app.add_song_to_user_playlist("Enxhi2803", "Favourite Songs", first_song)
    spotify_app.add_song_to_user_playlist("Enxhi2803", "Favourite Songs", second_song)

    songs = spotify_app.search_user_playlist("Enxhi2803", "Favourite Songs")
    print(songs)

    spotify_app.delete_song_from_user_playlist("Enxhi2803", "Favourite Songs", second_song)
    songs = spotify_app.search_user_playlist("Enxhi2803", "Favourite Songs")

    print(songs)

    songs = spotify_app.search_user_playlist("Enxhi2803", "Kot")

    print(songs)

    songs_author = spotify_app.search_user_artist("Enxhi2803", "Andi Shkoza")
    print(songs_author)


if __name__ == '__main__':
    main()
