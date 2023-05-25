class MovieLibrary:
    def __init__(self):##Her classın içinde mutlaka bir "__init__" vardır ve bu classı inşa eder. "__init__" fonksiyonu yazmasan bile gizli boş bir "__init__" fonksiyonu vardır ve classın içindeki tüm değerlere null atar.
        self.file = open("movies.txt", "a")##eşitliğin sağ tarafı fonksiyonun parametreleridir. Sol tarafı ise classın içine tanımladığın veriler.

    def append_movie(self):
        movie_name = input("Enter movie name: ")
        movie_genre = input("Enter movie genre: ")
        movie_year = input("Enter movie year: ")
        self.file.writelines(movie_name+" "+movie_genre+" "+movie_year+"\n")
    def seek_movie(self, key_value:str):
        filename = open("movies.txt", "r")

        for line in filename.readlines():
            if key_value in line:
                return line
        return "There is no movie related with entered key value"


while True:
    movie_library = MovieLibrary()
    chosen = input("""
    For movie appending press 1
    For movie seeking press 2
    Exit 3\n
    """)
    if chosen == "1":
        movie_library.append_movie()
    elif chosen == "2":
        key_value = input("Enter key value: ")
        found=movie_library.seek_movie(key_value=key_value)
        print("\n\n\n"+found)
    else:
        print("Please make correct selection!")