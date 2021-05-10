import os
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

base_op = create_engine('sqlite:///match.db')
base = declarative_base()


class Team(base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    teammate_id = Column(Integer, ForeignKey("teammates.id"))
    game_id = Column(Integer, ForeignKey("games.id"))


class Teammates(base):
    __tablename__ = "teammates"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    team = relationship('Team', backref='teammates')


class Game(base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True)
    team_1 = relationship('Team', backref='first_team')
    team_2 = relationship('Team', backref='second_team')
    score = Column(String, nullable=False)


base.metadata.create_all(base_op)

dbsession = sessionmaker(bind=base_op)
session = dbsession()

if not session.query(Team).count():
    session.add(Team(name="Los Angeles Lakers", teammate_id=1, game_id=1))
    session.add(Team(name="Chicago Bulls", teammate_id=2, game_id=2))
    session.add(Team(name="Washington Wizards", teammate_id=3, game_id=3))
    session.add(Team(name="Brooklyn Nets", teammate_id=4, game_id=4))
    session.add(Teammates(name="Jan", surname="Kowalski"))
    session.add(Teammates(name="Jan2", surname="Kowalski2"))
    session.add(Teammates(name="Jan3", surname="Kowalski3"))
    session.add(Teammates(name="Jan4", surname="Kowalski4"))
    session.add(Game(score="Coś"))
    session.add(Game(score="Bo"))
    session.add(Game(score="Nie znam"))
    session.add(Game(score="Się"))

session.commit()
