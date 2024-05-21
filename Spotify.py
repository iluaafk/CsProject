from User import User


class Spotify:

    def __init__(self):
        self.users = {}

    def add_user(self, username):
        if username not in self.users:
            self.users[username] = User(username)

    def create_playlist_for_user(self, username, playlist_name):
        if username in self.users:
            self.users[username].create_playlist(playlist_name)

    def delete_playlist_for_user(self, username, playlist_name):
        if username in self.users:
            self.users[username].delete_playlist(playlist_name)

    def add_song_to_user_playlist(self, username, playlist_name, song):
        if username in self.users:
            self.users[username].add_song_to_playlist(playlist_name, song)

    def search_user_playlist(self, username, playlist_name):
        if username in self.users:
            return self.users[username].search_playlist(playlist_name)
        else:
            return None

    def search_user_artist(self, username, artist):
        if username in self.users:
            return self.users[username].search_by_author(artist)
        return None

    def delete_song_from_user_playlist(self, username, playlist_name, song):
        if username in self.users:
            self.users[username].delete_song_from_playlist(playlist_name, song)
