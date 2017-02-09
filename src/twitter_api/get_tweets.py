import json
import sys
from client import *
import unicodedata
print("Ingrese Referencia para captura de Tweets")
q=input();

params={
'q':q,
#'until':"2016-12-28"
}
result=getAllTweets(params=params)

i=0
retrieved=[]
for t in result:
    i+=1
    retrieved.append({"i":i,"user":t["user"]["screen_name"],"msg":t["text"],"date":t["created_at"]})
file_name="tweets-"+q+".json"
print("Guardando Archivo: "+"tweets-"+q+".json...")
out_file = open("../../res/tweets/"+file_name,"w", encoding='utf-8')
json.dump(retrieved,out_file, indent=4) 
out_file.close()
print("Proceso Finalizado")
