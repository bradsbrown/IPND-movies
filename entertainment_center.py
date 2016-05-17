# media defines the class for movie info - description, cover art and trailer
import media
'''fresh_tomatoes will take the movie data, assemble the relevant pieces
into logical arrays, and use that information to generate a responsive webpage
to display all movies with their cover art and trailers'''
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # noqa
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # noqa
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

tombstone = media.Movie("Tombstone",
                        "The Earp brothers and Doc Holliday "
                        "take on the Cowboys"
                        " in Tombstone, AZ.",
                        "https://upload.wikimedia.org/wikipedia/en/7/71/Tombstoneposter.jpeg",  # noqa
                        "https://www.youtube.com/watch?v=XTWYKf5hXIg")

whiplash = media.Movie("Whiplash",
                       "An aspiring drummer struggles to achieve greatness",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/0/01/Whiplash_poster.jpg/220px-Whiplash_poster.jpg",  # noqa
                       "https://www.youtube.com/watch?v=7d_jQycdQGo")

martian = media.Movie("The Martian",
                      "A man gets marooned on Mars, and has to "
                      "fight to survive.",
                      "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",  # noqa
                      "https://www.youtube.com/watch?v=Ue4PCI0NamI")

guardians = media.Movie("Guardians of the Galaxy",
                        "A ragatag team has to work together to save "
                        "the entire galaxy from destruction.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/8/8f/GOTG-poster.jpg/220px-GOTG-poster.jpg",  # noqa
                        "https://www.youtube.com/watch?v=B16Bo47KS2g")

movies = [toy_story, avatar, tombstone, whiplash, martian, guardians]
fresh_tomatoes.open_movies_page(movies)
