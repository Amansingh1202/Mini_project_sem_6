import model

movie1 = model.Movie(id=1, movie_name="Iron Man (2008)", average_score=0)
movie2 = model.Movie(id=2, movie_name="The Amazing Spider-Man", average_score=0)
movie3 = model.Movie(
    id=3, movie_name="Star Wars: The Rise of Skywalker", average_score=0
)
movie4 = model.Movie(id=4, movie_name="Avatar (2009)", average_score=0)
movie5 = model.Movie(id=5, movie_name="Godzilla (2014)", average_score=0)
movie6 = model.Movie(id=6, movie_name="THOR (2011)", average_score=0)

model.db.session.add(movie1)
model.db.session.add(movie2)
model.db.session.add(movie3)
model.db.session.add(movie4)
model.db.session.add(movie5)
model.db.session.add(movie6)

model.db.session.commit()