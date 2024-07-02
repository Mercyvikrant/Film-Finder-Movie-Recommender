# Film-Finder-Movie-Recommender

# **Overview**

Welcome to the Movie Recommender/Film Finder! This project leverages user-based collaborative filtering to suggest movies you might enjoy based on your preferences
and the ratings given by other users. By analyzing user interactions and identifying patterns, our system provides personalized movie recommendations.

# **Dataset**

The system uses the following datasets, located in the data_sets directory:

movies.csv: Contains movie IDs, titles, and genres.

ratings.csv: Contains user ratings for movies.

# **Data Description**
1. movies.csv
   - This file contains movie details.
   - Columns: movieId, title, genres
     
2. ratings.csv
   - This file contains user ratings for movies.
   - Columns: userId, movieId, rating, timestamp
  
# **How It Works**

**The recommendation system follows these steps:**

1. Load Datasets: Reads the CSV files into pandas DataFrames.
2. Merge Data: Combines the movie and rating data to create a unified DataFrame.
3. User Input: Prompts the user to input a movie they like.
4. Find Similar Users: Identifies users who have highly rated the input movie.
5. Recommend Movies: Suggests other movies that these users have rated highly, excluding the input movie.



# **Examples**

**Here are some example movie titles you can use for testing the recommendation system:**

1. Forrest Gump (1994)
2. Heavy Metal (1981)
3. Hellraiser: Bloodline (1996)
4. Indiana Jones and the Temple of Doom (1984)
5. Interview with the Vampire: The Vampire Chronicles (1994)
6. Jerky Boys, The (1995)

# **Sample Output**

Enter the movie name that you like recommendation for = Jumanji (1995)

movie recommendation for users already watched that movies:-
Father of the Bride Part II (1995)

Grumpier Old Men (1995)

Heat (1995)

Toy Story (1995)

Waiting to Exhale (1995)








