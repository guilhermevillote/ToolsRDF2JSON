out_arquivo = open("output_final.json", "w+")
in_arquivo = open("own-pt.nt", "r")
out_arquivo.write("{\"dados\":[")
fix_control = 0
for linha in in_arquivo:
	fix_control += 1
	valores = linha.split()
	control = -1
	num = 0
	string = ["SUJEITO", "OBJETO", "PREDICADO"]
	for n in range( len(valores) ):
		if num < 3 :
			if valores[n].find("\"") == -1 & control<0:
				string[num] = valores[n]
				num += 1
			elif valores[n].find("\"") != -1:
				if valores[n].count("\"") == 1:
					if control < 0:
						string[num] = valores[n].replace("\"","").replace("\\","")
						control = +1
					else:
						string[num] = string[num]+" "+valores[n].replace("\"","").replace("\\","")
						control = -1
						num += 1
				elif valores[n].count("\"") == 2:
					string[num] = valores[n].replace("\"","").replace("\\","")
					num += 1
			else:
				valores[n].find("\"") == -1 & control>0
				string[num] = string[num] +" "+valores[n]
	if (fix_control == 1):
		out_arquivo.write("\n{\"Subject\":\""+string[0]+"\",\"Predicado\":\""+string[1]+"\",\"Object\":\""+string[2]+"\"},")
	elif (fix_control == 2):
		out_arquivo.write("\n{\"Subject\":\""+string[0]+"\",\"Predicado\":\""+string[1]+"\",\"Object\":\""+string[2]+"\"}")
	else: 
		out_arquivo.write(",\n{\"Subject\":\""+string[0]+"\",\"Predicado\":\""+string[1]+"\",\"Object\":\""+string[2]+"\"}")
out_arquivo.write("\n\n]}")
in_arquivo.close()
out_arquivo.close()