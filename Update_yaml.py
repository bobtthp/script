from ruamel import yaml
def json_to_yml(json):
	d = {
	'version' : json['version'],
	'service' : {
		json['docker'] : 
			{ 
		  	'image' : json['languages'] ,
		  	'port'  : 6379
			}
	           }
   	}
	try:
		with open(json['docker'] + '.yaml','w') as f:
			yaml.dump(d,f,Dumper=yaml.RoundTripDumper,indent=4)	
		return 0
	except Exception as E:
		print E
		
