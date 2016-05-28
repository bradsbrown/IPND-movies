# Fresh Tomatoes
Welcome to FreshTomatoes! This is a simple python script designed to create and present a web page with all of your favorite movies and some basic information about each!

# QuickStart Guide

Getting your page is pretty quick and easy, just follow a few quick steps:

1. Make sure you have 'media.py', 'fresh_tomatoes.py', and 'entertainment_center.py' contained in the same folder.
1. Using your editor of choice, open entertainment_center.py. This will be the only file you'll need to edit.
1. For each movie you want listed, add the following code:

  ``<movie-shortname> = media.Movie("<full-movie-name>","<movie-description>", "<box-art-link>", "<youtube-link>")``

  and fill in the areas in the '<>' with the described item. For example, to add Toy Story to your movies, you would add:

  `toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")`

  We have included some sample movies, which you can remove, replace, or keep as you like.
1. At the bottom of the file, edit the `movies = []` list to include the shortnames of all the movies in your code above. For example, if your had entries for movies with the shortnames toy_story, top_gun, and tombstone, your list would read:
`movies = [toy_story, top_gun, tombstone]`
1. Save your file, then open your terminal, navigate to the directory where these files are stored, type `python fresh_tomatoes.py`, and press Enter.
1. It should generate the display page for your movies, and open in your default browser. Just click on the cover art to watch the trailer. Enjoy!
