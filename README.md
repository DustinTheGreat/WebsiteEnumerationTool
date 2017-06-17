# WebsiteEnumerationTool
This script creates an object that you can leverage as premium hacking tool for website enumeration
### System Requirements
  1. `Sudo apt-get install Nmap`
  2. `Sudo apt-get install Whois`
  
### Python Package Requirements
   1. `pip install requests`
   
 
### Arguments

__required__

`
host should be in the following format i.e (_https://www.facebook.com_)
Test = HackTool(host)`

__optional__

`
_-O is a optinal Nmap argument_
...Test = HackTool(host, -O)
`
### Use
`
  ...Test = HackTool(host)
  ...Test.nmap_scan()
  ...Test.get_ip()
  ...Test.whois_lookup()

`




  
