#!/usr/bin/python3
#(c) 2017 by Dustin Roberts
#Use must have Nmap and Whois installed on your linux machine to make the most out of this program.
#mandatory packages: pip install requests

###############################################################################
#                                                                             #
#    This file is an object that you can import into your project             #
#                                                                             #
#    ReconnaissanceScanenr is free software: you can redistribute             #
#    it under the terms of the GNU General Public License as published by     #
#    the Free Software Foundation, either version 3 of the License, or        #
#    any later version.                                      		     	  #
#                                                                             #
#    This program is distributed in the hope that it will be useful,          #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            #
#    GNU General Public License for more details.                             #
#                                                                             #
#    You should have received a copy of the GNU General Public License        #
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.    #
###############################################################################

"""this module creates a object that you can use a premium Hacking Tool for enumeration"""


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
#the only mandatory argument is a hostname ie:'https://www.facebook.com'
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

	#get permissions
	def get_robots_txt(self, data=None):
		if self.url.endswith( '/' ):
			path = self.url
		else:
			path = self.url + "/"
			
		req = requests.get( path + "robots.txt", data )
		my_obj = json.loads(req.content)
		print("Robots.txt done!")
		print my_obj

	#must have Nmap isntalled on your machine
	def nmap_scan(self):
		if self.options is None:

			try:
				scan = subprocess.check_output(['nmap','-O', self.ip ])
				with open(self.file, 'wr') as res:
					res.write(scan)
			except Exception as e:
				print str(e)
				print('Could not retrieve whois_lookup ')
				logging.error('This message should go to the log file')

				#sys.exit(1)	
		else:
			blank = '-'
			blank.join(self.option)
			option = blank


			try:
				scan = subprocess.check_output(['nmap',option, self.ip ])
				with open(self.file, 'wr') as res:
					res.write(scan)
			except Exception as e:
				print str(e)
				print('Could not retrieve whois_lookup ')
				logging.error('This message should go to the log file')





	def whois_lookup(self):
		try:
			with open(self.file, 'wr') as res:
				res.write(scan)
		except Exception as e:
			print str(e)
			print('Could not retrieve whois_lookup ')
			logging.error('This message should go to the log file')
			pass


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-H', '--hostname', type=str, required=True, 
                    help='Host name, IP Address ie. https://www.facebook.com')
	parser.add_argument('-O', '--options', required=False, 
                    help='pass any Nmap options ex. -A, -O, -sT ')


	args = parser.parse_args()

	def main(host, value=None):
		test = HackTool(host, value)
		print test	
	main(args.hostname, args.options)
