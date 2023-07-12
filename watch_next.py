import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def find_similar_movie(description):
    # Read the movie descriptions from the movies.txt file
    with open('movies.txt', 'r') as file:
        movie_descriptions = file.readlines()

    # Preprocess the descriptions
    processed_descriptions = [re.sub(r'[^\w\s]', '', desc.lower()) for desc in movie_descriptions]

    # Add the given description to the list of processed descriptions
    processed_descriptions.append(re.sub(r'[^\w\s]', '', description.lower()))

    # Create TF-IDF vectors for the processed descriptions
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(processed_descriptions)

    # Calculate cosine similarities between the given description and all other descriptions
    similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])

    # Find the index of the most similar movie
    most_similar_index = np.argmax(similarities)

    # Return the title of the most similar movie
    movie_titles = ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E', 'Movie F', 'Movie G', 'Movie H', 'Movie I', 'Movie J']
    return movie_titles[most_similar_index]

# usage example
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
similar_movie = find_similar_movie(description)
print(similar_movie)

# StackOverflow for reference