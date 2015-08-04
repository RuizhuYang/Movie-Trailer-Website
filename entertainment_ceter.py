import media
import fresh_tomatoes

###construct instance of movie taken
taken = media.Movie("Taken",
                    "http://www.moviexclusive.com/Files/622879poster.jpg",
                    "https://www.youtube.com/watch?v=3Tz9tQr1Zgo",
                    "2008")
 ###construct instance of movie edge of tomorrow
edge_tomorrow = media.Movie("Edge Of Tomorrow",
                            "http://upload.wikimedia.org/wikipedia/en/f/f9/Edge_of_Tomorrow_Poster.jpg",
                            "https://www.youtube.com/watch?v=5xuBlpp4ssg",
                            "2014")

###construct instance of movie gods and kings
gods_and_king = media.Movie("Gods and Kings",
                            "http://0c27d848a8e38cd7431e-9022dd8e0be2d885290040dc412b102c.r0.cf1.rackcdn.com/2014/12/movies-exodus-gods-and-kings-poster-01.jpg",
                            "https://www.youtube.com/watch?v=t-8YsulfxVI",
                            "2014")
                            
 ###construct instance of movie kingsman
kingsman = media.Movie("Kingsman",
                       "http://ia.media-imdb.com/images/M/MV5BMTkxMjgwMDM4Ml5BMl5BanBnXkFtZTgwMTk3NTIwNDE@._V1_SX640_SY720_.jpg",
                       "https://www.youtube.com/watch?v=m4NCribDx4U",
                       "2015")
###construct instance of movie lucy                       
lucy = media.Movie("Lucy",
                   "http://upload.wikimedia.org/wikipedia/zh/1/14/Lucy_(2014_film)_poster.jpg",
                   "https://www.youtube.com/watch?v=MVt32qoyhi0",
                   "2014")

###construct instance of movie interstellar
interstellar = media.Movie("Interstellar",
                           "http://ia.media-imdb.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SX640_SY720_.jpg",
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA",
                           "2014")

### build a array of movies which include all the Movie instances above
movies = [taken, edge_tomorrow, gods_and_king, kingsman, lucy, interstellar]

### use method open_movie_page of fresh_tomatoes module to create a page of my movies
fresh_tomatoes.open_movies_page(movies)

          
                          
