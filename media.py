import webbrowser

class Movie():
    ###The constructor of Movie
    def __init__(self, movie_title, movie_image, movie_trailer, year):
        self.title = movie_title
        self.poster_image_url = movie_image
        self.trailer_youtube_url = movie_trailer
        self.year = year
        

    ## Show the trailer of movie
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
