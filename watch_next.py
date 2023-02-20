# First we import spacy.  
import spacy
nlp = spacy.load('en_core_web_md')

# Here we place the hulk description that we will compare the other movies with.
description = '''Will he save their world or destroy it? 
When the Hulk becomes too dangerous for the Earth, 
the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace.
Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.'''

# We use open the 'movie.txt' file to get all the descriptions we need to compare.
with open("movies.txt", "r") as files:
   movies = [line.strip() for line in files]
    
  
# The function below cheacks the similarity between the Hulk and other movies.
# It then gives each movie description a similarity index so the more similar movies have a higher index.
# Finally the movie with the highest index is returned
def movie_finder(descriptions):
    similarities = [nlp(description).similarity(nlp(movie)) for movie in movies]
    index_most_similar = similarities.index(max(similarities))
    return movies[index_most_similar]

movie_finder(description)
print(movie_finder(description))