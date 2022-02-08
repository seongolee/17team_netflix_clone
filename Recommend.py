import pandas as pd
import numpy as np

ratings = pd.read_csv('static/recommendation/ratings.csv')
movies = pd.read_csv('static/recommendation/movies.csv')

# 데이터프레임을 출력했을때 더 많은 열이 보이도록 함
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 300)
# movieId를 기준으로 ratings 와 movies 를 결합함
movie_ratings = pd.merge(ratings, movies, on='movieId')
print(movie_ratings)


def item_based_recommenation():
    user_title = movie_ratings.pivot_table('rating', index='title', columns='userId')

    user_title = user_title.fillna(0)
    print(user_title)

    from sklearn.metrics.pairwise import cosine_similarity

    item_based_collab = cosine_similarity(user_title, user_title)
    print(item_based_collab)

    item_based_collab = pd.DataFrame(item_based_collab, index=user_title.index, columns=user_title.index)
    print(item_based_collab)

    # 불가살과 비슷하게 유저들로부터 평점을 부여받은 영화들은?
    print(item_based_collab['불가살'].sort_values(ascending=False)[1:11])

item_based_recommenation()
item_based_collab['불가살'].sort_values(ascending=False)[1:10]