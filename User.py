from Playlist import Playlist


class User:

    def __init__(self, username):
        self.username = username
        self.playlists = {}

    def create_playlist(self, playlist_name):
        if playlist_name not in self.playlists:
            self.playlists[playlist_name] = Playlist(playlist_name)

    def delete_playlist(self, playlist_name):
        if playlist_name in self.playlists:
            del self.playlists[playlist_name]
            print(f"Playlist '{playlist_name}' deleted successfully")
        else:
            print(f"Playlist '{playlist_name}' not found")

    def add_song_to_playlist(self, playlist_name, song):
        if playlist_name in self.playlists:
            self.playlists[playlist_name].add_song(song)

    def search_playlist(self, playlist_name):
        if playlist_name in self.playlists:
            return self.playlists[playlist_name].list_song()
        else:
            return None

    def search_by_author(self, author_name):
        songs = []
        for playlist_name, playlist in self.playlists.items():
            songs.append(playlist.search_by_author(author_name))
        return songs

    def delete_song_from_playlist(self, playlist_name, song):
        if playlist_name in self.playlists:
            self.playlists[playlist_name].delete_song(song)

