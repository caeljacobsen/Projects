# An application that attempts to connect to a website or server every so many minutes or a given time and check if it is up.
# If it is down, it will notify you by email or by posting a notice on screen.

import sys


if __name__ == '__main__':
	while(True):
		print("Checking site")
		