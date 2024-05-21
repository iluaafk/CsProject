from LinkedList import LinkedList


class Playlist:

    def __init__(self, name):
        self.name = name
        self.songs = LinkedList()

    def add_song(self, song):
        self.songs.append(song)

    def list_song(self):
        return self.songs.display()

    def delete_song(self, song):
        self.songs.delete(song)

    def search_by_author(self, author_name):
        matching_songs = []
        current = self.songs.head  # Start at the head of the linked list

        while current:
            if current.data.artist == author_name:  # Access artist attribute of the song
                matching_songs.append(current.data)
            current = current.next

        return matching_songs
