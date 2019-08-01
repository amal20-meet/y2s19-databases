from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(topic,name,rating):
	Narticle = Knowledge(
		topic = topic,
		name = name,
		rating = rating)
	session.add(Narticle)
	session.commit()
	
# add_article("stuff", "Zain", 10)
# add_article("hello", "Juna", 2)
# add_article("Share", "Amal", 10)
# add_article("Unicorn", "Shir", 9)
# add_article("Whatever", "Someone", 5)

def query_all_articles():

	all_article = session.query(Knowledge).all()
	return all_article

# print(query_all_articles())

def query_article_by_topic(their_topic):
	article_by_topic = session.query(Knowledge).filter_by(topic = their_topic).first()
	return article_by_topic

# print(query_article_by_topic("stuff"))

def delete_article_by_topic(their_topic):
	session.query(Knowledge).filter_by(topic=their_topic).delete()
	session.commit()

def delete_all_articles():
	session.query(Knowledge).delete()
	session.commit()

def edit_article_rating(title,x):
	knowledge = session.query(Knowledge).filter_by(topic = title).first()
	knowledge.rating=x
	session.commit()

