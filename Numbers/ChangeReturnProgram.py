# The user enters a cost and then the amount of money given.
#The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.

import sys

class USD(object):
	"""
	Object that contains the definition for the most used United States Dollar currency
	Can return the best change when given a specific money value (in dollars)
	"""
	def __init__(self):
		self.coins = ['Hundred Dollar', 'Fifty Dollar', 'Twenty Dollar', 'Ten Dollar', 'Five Dollar', 'Dollar','Quarter','Dime','Nickel','Penny']
		self.coinVals = [10000, 5000, 2000, 1000, 500, 100, 25, 10, 5, 1]
	#takes two float values
	#returns list containing tuples that contain (amount of money, name of coin)
	def getBestChange(self, cost, moneyGiven):
		"""
		This function calculates the best change for a given transaction.
		cost is the amount that was to be charged
		moneyGiven is the amount that was paid.
		Returns the best change available given the currency
		"""
		change = []
		#print(str(cost) + "," + str(moneyGiven))
		moneyGiven = moneyGiven - cost
		moneyGiven = int(round(moneyGiven * 100, 0)) #get cents, base unit of currency, use round to negate round off error. Funny Coincidence
		print(moneyGiven)
		if(moneyGiven > 0):
			for i in range(len(self.coinVals)):
				#If it's zero we don't need to include it.
				if(int(moneyGiven/self.coinVals[i]) != 0):
					change.append((int(moneyGiven/self.coinVals[i]), self.coins[i]))
				moneyGiven = ( moneyGiven % self.coinVals[i] )
		#Run through this loop if the amount isn't needed to complete the transaction
		else:
			for i in range(len(self.coinVals)):
#			If it's zero we don't need to include it.
				if(int(moneyGiven/self.coinVals[i]) != 0):
					change.append((int(moneyGiven/self.coinVals[i]), self.coins[i]))
				moneyGiven = (moneyGiven % -self.coinVals[i])
		return change
if __name__ == '__main__':
	usd = USD()
	print(usd.getBestChange(10.99, 20.00))
	print(usd.getBestChange(20.00, 13.25))
	print(usd.getBestChange(999.99, 1000.00))
	#not going to make user input. testing is adequate