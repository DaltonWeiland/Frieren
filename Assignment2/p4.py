
class Show:
    #_genre is abstracted away with the property attribute and accessed by using genre
    def __init__(self, genre, title):
        self._genre = genre
        self.title = title

    def _get_genre(self):
        return self._genre
    
    def _set_genre(self, genre):
        print("Uppdated Genre")
        self._genre = genre

    def _delete_genre(self):
        del self._genre

    genre = property(fget=_get_genre,fset=_set_genre,fdel=_delete_genre,doc=None)

def main():
    show1 = Show("Action", "The Amazing Show")
    show1.genre = 'Comedy'
    print(show1.genre)


main()