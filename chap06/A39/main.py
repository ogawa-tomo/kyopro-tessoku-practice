N = int(input())


class Movie:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end

    def __repr__(self):
        return f"[start: {self.start}, end: {self.end}]"


movies: list[Movie] = []
for _ in range(N):
    L, R = map(int, input().split())
    movies.append(Movie(L, R))
movies.sort()
# print(movies)
watched_movies: list[Movie] = []

t = 0  # 現在時刻
for movie in movies:
    if movie.start >= t:
        watched_movies.append(movie)
        t = movie.end
# print(watched_movies)
print(len(watched_movies))
