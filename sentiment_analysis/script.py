import model

new_movie1 = model.Movie(movie_name="Iron Man (2008)", average_score=0)
new_movie2 = model.Movie(movie_name="The Amazing Spider-Man", average_score=0)
new_movie3 = model.Movie(movie_name="Star Wars: The Rise of Skywalker", average_score=0)
new_movie4 = model.Movie(movie_name="Avatar (2009)", average_score=0)
new_movie5 = model.Movie(movie_name="Godzilla (2014)", average_score=0)
new_movie6 = model.Movie(movie_name="THOR (2011)", average_score=0)
model.db.session.add(new_movie1)
model.db.session.add(new_movie2)
model.db.session.add(new_movie3)
model.db.session.add(new_movie4)
model.db.session.add(new_movie5)
model.db.session.add(new_movie6)

model.db.session.commit()