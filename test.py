import os
import subprocess
import re
import requests
#Importing io for encoding
#import io
# Function to get robots.txt file
#Setting up
import json
import sys
import logging
import argparse

class HackTool(object):

	LOG_FILENAME = 'example.log'
	logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

	def __init__(self, host, options=None):
		self.options = options
		self.host = host
		self.url = self.get_tld(host)
		self.ip = self.get_ip()

	
	def __str__(self):
		return self.url

	def make_dir(self):
		if os.path.exists('scans'):
			pass
		else:
			os.mkdir(scans)

	def  make_file(self):
		try:
			if os.path.isfile('scanON{}.txt'.format(self.url)):
				pass
			else:
				return path + 'scanON{}.txt'.format(self.url)
		except:
			print('there was a problem')
				

	def get_tld(self, host):
		new_url = str()
		remove_words = ['https://www.', 'http://www.']
		for word in remove_words:
			if word in host:
				new_url = host.replace(word, '')
			else:
				pass
		logging.error('This message should go to the log file')

		return new_url


	def get_ip(self):
		final = ' '
		results = subprocess.check_output(['host', self.url])
		line =  results.splitlines()[0]
		words =  str(re.findall(r'[+-]?\d+', line))
		for word in words:
			final.join(word)
		return final

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-H', '--hostname', type=str, required=True, 
                    help='Host name, IP Address')
	parser.add_argument('-O', '--options', required=False, 
                    help='Pass in any Nmap options ex. -A, -O, -sT ')


	args = parser.parse_args()

	def main(host, value=None):
		test = HackTool(host, value)
		print test	
	main(args.hostname, args.options)
