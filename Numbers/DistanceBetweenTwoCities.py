# Calculates the distance between two cities and allows the user to specify a unit of distance.
#This program may require finding coordinates for the cities like latitude and longitude.

import sys

def Convert(distance, initUnit, endUnit):

class Coord(object):
	def __init__(self, deg = 0, min = 0, sec = 0, sign = "+"):
		self.degree = deg
		self.minute = min
		self.second = sec
	def getCoord(self):
		return (self.degree, self.minute, self.second)
	def getDegree(self):
		return self.degree + self.minute/60 + self.second/60/60
	
class EarthCoord(object):
	def __init__(self, lat, long):
		if(len(list(lat)) != 4):
			lat = [0, 0, 0, '+']
		if(len(long) != 4):
			long = [0, 0, 0, '+']
		self.latitude = Coord(lat[0], lat[1], lat[2]) 	#[Degrees, Minutes, Seconds] Positive is Eastern, Negative is Western
		self.longitude = Coord(long[0], long[1], long[2])	#[Degrees, Minutes, Seconds] Positive is North, Negative is Southern
	def setLatitude(deg, min, sec):
		self.latitude.degree = deg
		self.latitude.minute = min
		self.latitude.second = sec
	def setLongitude(deg, min, sec):
		self.longitude.degree = deg
		self.longitude.minute = min
		self.longitude.second = sec
	# measures the distance between itself and another coordinate
	def distance(self, coordinate):
		r = 6371 #Average Radius of the earth
		#implement Haversine Distance formula
		lat1 = math.radians(self.latitude.getDegree())
		lat2 = math.radians(coordindate.getDegree())
		deltaLat = math.radians(self.latitude.getDegree() - coordinate.getDegree())
		deltaLong = math.radians(self.longitude.getDegree() - coordinate.getDegree())
		a = math.sin(deltaLat/2) ** 2 + math.cos(lat1) * math.cos(lat2) * (math.sin(deltaLong/2) ** 2)
		c = 2*math.atan2(math.sqrt(a), math.sqrt(1-a))
		distance = r * c
		return distance

if __name__ == '__main__':
	portland = EarthCoord([45,52,36,'+'],[122,67,50,'-'])
	denver = EarthCoord([39,73,92,'+'], [104,98,42,'-'])
	print("The distance from Portland to Denver is:")
	print(portland.distance(denver))