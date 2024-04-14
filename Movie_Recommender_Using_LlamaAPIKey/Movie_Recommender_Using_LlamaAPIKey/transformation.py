import pandas as pd

# 读取用户数据
users_cols = ['UserID', 'Gender', 'Age', 'Occupation', 'Zip-code']
users = pd.read_csv('users.dat', sep='::', engine='python', header=None, names=users_cols)

# 读取电影数据
movies_cols = ['MovieID', 'Title', 'Genres']
movies = pd.read_csv('movies.dat', sep='::', engine='python', header=None, names=movies_cols, encoding='latin1')

# 读取评分数据
ratings_cols = ['UserID', 'MovieID', 'Rating', 'Timestamp']
ratings = pd.read_csv('ratings.dat', sep='::', engine='python', header=None, names=ratings_cols)

# 将数据写入CSV文件
users.to_csv('users.csv', index=False)
movies.to_csv('movies.csv', index=False)
ratings.to_csv('ratings.csv', index=False)