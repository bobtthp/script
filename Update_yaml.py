from ruamel import yaml
d = {
'version' : '1.0',
'service' : {'redis' : 
		{ 
		  'image' : 'redis' ,
		  'port'  : 6379
		},
              'db' :
		{
		  'image' : 'mysql',
		  'networks' : 'host'
		} 
	    }
   }


with open('test.yaml','w') as f:
	yaml.dump(d,f,Dumper=yaml.RoundTripDumper,indent=4)	
