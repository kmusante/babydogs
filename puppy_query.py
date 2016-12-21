from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from puppies import *
import datetime

engine= create_engine('sqlite:///puppyshelter.db')

Session=sessionmaker(bind=engine)

session=Session()
# 1. Query all of the puppies and return the results in ascending alphabetical order
def getDogsAlphabetically():
	puppies=session.query(Puppy).order_by(Puppy.name).all()
	for puppy in puppies:
		print puppy.id
		print puppy.name
		print puppy.gender
		print puppy.dateOfBirth
		print puppy.picture
		print puppy.shelter_id
		print puppy.weight
		print "\n"

#2. Query all of the puppies that are less than 6 months old organized by the youngest first
def getYoungPups():
	sixMonthsAgo=datetime.date.today()-datetime.timedelta(6*365/12)
	puppies=session.query(Puppy).filter(Puppy.dateOfBirth> sixMonthsAgo).order_by(Puppy.dateOfBirth.desc()).all()
	for puppy in puppies:
		print puppy.name
		print puppy.dateOfBirth
		print "\n"

#3. Query all puppies by ascending weight
def getWeight():
	puppies=session.query(Puppy).order_by(Puppy.weight).all()
	for puppy in puppies:
	    print puppy.name
	    print puppy.weight
	    print puppy.id
	    print "\n" 

#4. Query all puppies grouped by the shelter in which they are staying
def shelterQuery():
	puppies=session.query(Puppy).order_by(Puppy.shelter_id).all()
	for puppy in puppies:
	    print puppy.name
	    print puppy.shelter_id
	    print "\n"

#getYoungPups()
#getDogsAlphabetically()
getWeight()
#shelterQuery()
