# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 00:30:18 2024

@author: Vikrant sinha
"""
import numpy as np
import pandas as pd

i=0
j=0

links_df = pd.read_csv("D:\\Python_movie recommendation\\data_sets\\links.csv")
movies_df = pd.read_csv("D:\\Python_movie recommendation\\data_sets\\movies.csv")
tags_df = pd.read_csv("D:\\Python_movie recommendation\\data_sets\\tags.csv")
ratings_df = pd.read_csv("D:\\Python_movie recommendation\\data_sets\\ratings.csv")

df = movies_df.merge(ratings_df, on='movieId')

# movies liked by the other persons of same genre

M_j =input("Enter the movie name that you like reccomendation for =")
recommended_movies = []


movie_db = df[df['title'] == M_j]\
            .sort_values(by='rating', ascending=False)


for user in movie_db.iloc[:5]['userId'].values:
    
    rated_movies = df[df['userId'] == user]
    
    rated_movies = rated_movies[rated_movies['title'] != M_j]\
                    .sort_values(by='rating', ascending=False)\
                    .iloc[:5]
    
    recommended_movies.extend(list(rated_movies['title'].values))
    
recommended_movies = np.unique(recommended_movies)

print("\nmovie reccommendation for users already watched that movies:-\n")

for movie in recommended_movies:
    print(movie)

print("----------------------------------------------------------------------------------")
    
    



# movies names
