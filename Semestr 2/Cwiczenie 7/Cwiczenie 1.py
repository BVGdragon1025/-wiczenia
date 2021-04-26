import os
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

base_op = create_engine('sqlite:///moviedb.db')
base = declarative_base()


class Movies(base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    director = Column(String, nullable=False)
    actors = Column(String, nullable=False)
    platform_id = Column(Integer, ForeignKey('platforms.id'))


class Platforms(base):
    __tablename__ = "platforms"
    id = Column(Integer, primary_key=True)
    platform_name = Column(String, nullable=False)
    movie = relationship('Movies', backref='platforms')


base.metadata.create_all(base_op)

dbsession = sessionmaker(bind=base_op)
session = dbsession()

if not session.query(Platforms).count():
    session.add(Platforms(platform_name="Netflix"))
    session.add(Platforms(platform_name="HBO Go"))
    session.add(Platforms(platform_name="Amazon Prime"))

session.commit()


class MovieApp:
    def __init__(self, title, director, actors, platform_name):
        self.title = title
        self.director = director
        self.actors = actors
        self.platform_name = platform_name

    def movie_add(self):
        self.title = input("Podaj nazwę filmu: ")
        self.director = input("Podaj reżysera: ")
        self.actors = input("Podaj aktorów: ")
        self.platform_name = int(input("Wybierz platformę: [1]Netflix, [2]HBO Go, [3]Amazon Prime: "))

        if self.platform_name == 1:
            session.add(Movies(title=self.title, director=self.director, actors=self.actors,
                               platform_id=self.platform_name))
        elif self.platform_name == 2:
            session.add(Movies(title=self.title, director=self.director, actors=self.actors,
                               platform_id=self.platform_name))
        else:
            session.add(Movies(title=self.title, director=self.director, actors=self.actors,
                               platform_id=self.platform_name))
        session.commit()
        print("Film dodany!")

    def movie_show(self):
        print("Lista filmów w bazie: ")
        for movies in session.query(Movies).join(Platforms).all():
            print(movies.id, movies.title, movies.director, movies.actors, movies.platforms.platform_name)
        print()


# MovieApp.movie_add(MovieApp)
MovieApp.movie_show(MovieApp)
