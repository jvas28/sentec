import os
import json
def getDataCollection():
	path="../res/tweets/"
	dirs=os.listdir(path)
	print ("Escoja la coleccion de tweets para el proceso:")
	menu_index=1;
	for file in dirs:
	   print(str(menu_index)+") "+file)
	   menu_index+=1
	selected=input()
	if "json" in dirs[int(selected)-1]:
		json_data=json.loads(open(path+"/"+dirs[int(selected)-1]).read())
	else:
		json_data=[{"msg":m} for m in open(path+"/"+dirs[int(selected)-1]).readlines() ]
	return json_data
