import json
import os

facts=[ "ansible_hostname", "ansible_architecture", "ansible_distribution" ,"ansible_memtotal_mb" , 
      "ansible_os_family" , "ansible_processor_count" ]
factdir='/tmp/facts/'

for filename in os.listdir(factdir):
	print factdir + filename
	with open(factdir + filename) as json_file:
    		json_data = json.load(json_file)
    		if json_data.has_key('ansible_facts'):
    			for i in range(len(facts)):
				if json_data.has_key(['ansible_facts'][facts[i]]):
					print facts[i] + ": " + str(json_data['ansible_facts'][facts[i]])
		else: 	
    			for i in range(len(facts)):
				if json_data.has_key(facts[i]):
					print facts[i] + ": " + str(json_data[facts[i]])
