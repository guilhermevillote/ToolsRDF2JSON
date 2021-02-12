def analyser1(word):
    if( word.find(":") == -1 ):
        return False
    else:
        return True

def analyser2(word):
    if( word.find("@") == -1 ):
        return False
    else:
        return True



out_arquivo = open("Dt_Neymar.nt", "w+")
in_arquivo = open("Dt_Neymar.json", "r")
#out_arquivo.write("{\"dados\":[")
fix_control = 0
ctrl = 0
next(in_arquivo)
for linha in in_arquivo:
    n_elem = 0
    string = []
    separacao = linha.split(",")
    if(len(separacao) > 2):
        for n in range( len(separacao) ):
            if(n_elem < 3):
                valores = separacao[n].split(": ")
                res = valores[1].replace("}", "").replace("\n","")
                if(analyser1(res)):
                    res = res.replace("\"", "")
                elif(analyser2(res)):
                    gui1 = res.split("@")
                    res = gui1[0]+"\""+"@"+gui1[1][0]+gui1[1][1]
                string.append(res)
                n_elem += 1
    #print(string)
    if(string):
        if(ctrl > 0):
        #print(string)
            out_arquivo.write(  "\n"+
                                "<"+string[0]+">"+" "+
                                "<"+string[1]+">"+" "+
                                "<"+string[2]+">"+" .")
        else: 
            out_arquivo.write(  "<"+string[0]+">"+" "+
                                "<"+string[1]+">"+" "+
                                "<"+string[2]+">"+" .")
    ctrl += 1
		
#out_arquivo.write("\n\n]}"
in_arquivo.close()
out_arquivo.close()