import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re
from xlrd import open_workbook
import numpy as np
import sys
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from numpy import dot
from numpy.linalg import norm

raza = ["negro","color carbón","esto no es África","se te acabó la tinta","sin derechos","indio verga","mono","mono verga","mono hijo de puta","negro cabrón","negro hijo de puta", 
"indio mama verga","negro enfermo","serrano bobo","costeño ladrón","gringo imbécil","serrano hijo de puta","mono ediondo","mono conche tu madre","negro pendejo",
"negro esclavo","negro verga", "negro de mierda", "mono infeliz", "indio estúpido", "negro ignorante", "negro asqueroso", "indio infeliz","indio imbécil", "longo", 
"longo feo", "negro miedo", "indio asqueroso", "longo estúpido", "negra", "longo pasposo", "longo pendejo ", "mono infeliz", "mono puto", "longo verga", "negro puto",
"india puerca", "negra asco", "asco de negros", "indios sucios ", "longos asquerosos" ,"indio","longa", "mono asco","imbecil", "hijo puta","mamaracho", "adefesioso",
"ruliman","paisano","indio mmvrg","indio hdp","indio hp","mono mmvrg","mono hp","mono cvrg","mono vrg","mono hdp","negro sucio","indio sucio","mono sucio",
"anda vender cocada","negro mal parido","costeño mal parido","indio come papa"]

genero = ["loca", "puta", "sirvienta", "marrana", "ignorante", "mujer tenías que ser", "a cocinar", "mamacita", "perra", "puto", "zorra", "indecente", "cochina","cochino", 
"zafada", "loco","zafado", "hombre tenías que ser", "patán", "cojuda", "cojudo", "desgraciado", "desgraciada", "analfabeto","analfabeta", "cornudo", "cornuda","cornudos", 
"perra de mierda","facilota","chucha","reflechucha","chepa","verga","mierda","cabron","cabrón","gil","retrasado","lelo","porqueria","apestoso","maldito","a la cocina","menso",
"mensa","estupida","estupido","cachudo","cachuda","bruto","delicada","delicado","bruta","tonta","tonto","zopenco","zopenca","tarado","tarada","imbécil","puta barata",
"chucha apestoza","sapa de mrd","sapo cabrón", "idiota","putita","putota","reputa","triplehijueputa","tontos"]

orientacion = ["maricon de mierda","virado","maricon", "marica de mierda", "del otro bando", "menestra puto", "maricon imbécil", "gay asco", "gay de verga", 
"maricas asquerosos", "pedazos putos", "traga pitos","muerde almohadas", "culo flojo", "maricon imbecil", "marica", "gay", "menestron", "menestra","pajero",
"huevon","puñal","marimacha","afeminado","nena","nenita","niña","princesa","princeso","veado","boiola","bolleras","poco hombre","sopla nucas","intento de hombre","chupamela","chupa pitos","hembra",
"reculeado","chullo huevo","puto de mierda","puto cagón","come pitos","marica reflechuchatumadre","chucha floja","triple homosexual","tetranutra","chupa huevos","chupa bolas","tortillera","lesbiana la puta tu madre",
"puñeta","falta de huevos","lesbiana de mrd","maricón","maricona","hermafrodita","femina","machona","mixto","mariposon","maricota","invertido","joto","muerdealmohadas","mariquita",
"pinche joto","mamapinga","mariconcito","putito"]

edad = ["enano cara verga","guambra caca","come verga enano","niño hijo de puta","enano castroso","tu madre te cagó","enano hijo de puta","guambra asco", 
"enano gil", "viejo de mierda", "enano ciego", "vieja inútil", "chamo imbécil", "guambra verga", "mocosa", "mocosos", "verga de chamos", "guambra coco", 
"chamo coco", "enano puto", "majadero", "majadera", "adoptada", "adoptado", "aborto", "cara de vrga" , "hijo de puta" , "mocoso pendejo", "guambra majadero", "guambra majadera", 
"mocosa inútil ", "mocoso malagradecido", "mocoso malagradecido ","mal agradecida", "mocoso mantenido", "mimado", "mocosa mantenida", "mimada",  "jodida", "jodido", "altanero",
"altanera", "verga de juventud", "viejo lento","enano verga","guambra caca", "mocoso", "viejo verga", "flacido","enano","marrano","gordo", "puerco","cerdo",
"chancho","esqueleto","guambra vrg","mocosa mal parida","guambra metido","condon roto","enano cabrón","mocoso gil","chamo vrg","viejo metido","viejo sapo","viejo chismoso",
"mocoso bueno para nada","guambra castroso","guambra","viejo mal parido","mocoso mal educado"]
raza = list(set(raza))

genero = list(set(genero))

orientacion = list(set(orientacion))

edad = list(set(edad))

#NORMALIZAR LISTAS FIJAS
def eliminar_stopwords(texto, stopwords):
    return ' '.join([word for word in texto.split(' ') if word not in stopwords])

def normList(text):
  vec = []
  for i in range(len(text)):
    a,b = 'áéíóúüñÁÉÍÓÚÜÑ','aeiouunAEIOUUN'
    til=str.maketrans(a,b)
    s=text[i].translate(til)
    d2 = re.sub('[^A-Za-z0-9]+', ' ', s)
    word = d2.lower()
    n = stopwords.words("spanish")
    word2=eliminar_stopwords(word,n)
    word2=word2.split()
    stemmer = PorterStemmer()
    l = []
    for i in word2:   
      l.append(stemmer.stem(i))
    vec.append(l)
  return vec

def normalizar(text):
  a,b = 'áéíóúüñÁÉÍÓÚÜÑ','aeiouunAEIOUUN'
  til=str.maketrans(a,b)
  s=text.translate(til)
  d2 = re.sub('[^A-Za-z0-9]+', ' ', s)
  word = d2.lower()
  n = stopwords.words("spanish")
  n.append("si")
  n.append("asi")
  n.append("un")
  n.append("eres")
  word2=eliminar_stopwords(word,n)
  word2=word2.split()
  stemmer = PorterStemmer()
  l = []
  for i in word2:   
    l.append(stemmer.stem(i))
  return l

raza = normList(raza)
genero = normList(genero)
orientacion = normList(orientacion)
edad = normList(edad)

def jaccard(grupo1, grupo2):
	interseccion = len(set(grupo1).intersection(set(grupo2)))
	union = len (set(grupo1).union(set(grupo2)))
	return interseccion / union

def discriminatorio1(text):
  text = normalizar(text)
  va = []
  vb = []
  vc = []
  vd = []
  vt = []
  for i in range(len(text)):
    t = [text[i]]
    for j in range(0,28):
      va.append(jaccard(t,raza[j]))
      vb.append(jaccard(t,genero[j]))
      vc.append(jaccard(t,orientacion[j]))
      vd.append(jaccard(t,edad[j]))
  sr = np.sum(va)
  sg = np.sum(vb)
  so = np.sum(vc)
  se = np.sum(vd)
  
  st = sr+sg+so+se
  if sr>0:
    vt.append("Discriminación por Raza en: "+str(round((sr*100)/st,2))+"%")
  if sg>0:
    vt.append("Discriminación por Género en: "+str(round((sg*100)/st,2))+"%")
  if so>0:
    vt.append("Discriminación por Orientación Sexual en: "+str(round((so*100)/st,2))+"%")
  if se>0:
    vt.append("Discriminación por Edad en: "+str(round((se*100)/st,2))+"%")
  if st==0:
    vt.append("El texto no tiene ningun tipo de discriminación")
  return "\n".join(vt)

###COSENO VECTORIAL###
r = set(np.concatenate(raza))
r = ",".join(r)

g = set(np.concatenate(genero))
g = ",".join(g)

o = set(np.concatenate(orientacion))
o = ",".join(o)

e = set(np.concatenate(edad))
e = ",".join(e)

def discriminatorio2(text):
  txt = ",".join(normalizar(text))
  vr = []
  tr = [r]+[g]+[o]+[e]+[txt]

  CountVec = CountVectorizer(ngram_range=(1,1), 
                            stop_words='english')
  Count_data = CountVec.fit_transform(tr[0:len(tr)])
 
  #cv_dataframe=pd.DataFrame(Count_data.toarray(),columns=CountVec.get_feature_names())
  cv_dataframe=pd.DataFrame(data=Count_data.toarray(), columns=CountVec.get_feature_names_out())
  df = 1+np.log10(cv_dataframe)
  df.replace([np.inf,-np.inf],0,inplace=True)

  idf = np.log10(len(tr)/df)
  idf.replace([np.inf,-np.inf],0,inplace=True)

  nor= idf / np.sqrt(np.sum(idf**2))
  nor = nor.to_numpy()

  va = []
  i = 0
  while i<len(tr):
    list1 = nor[i]
    for j in range(len(tr)):
      list2 = nor[j]
      va.append(dot(list1, list2)/(norm(list1)*norm(list2)))
    i+=1

  va=np.round(va,2)
  es=np.reshape(va, (len(tr),len(tr)), order='C')
  mat=np.array(es)

  dis = mat[len(tr)-1,0:len(tr)-1]
  sum = np.sum(dis)
  porce = [0,0,0,0]
  discrim=[]
  if dis[0]>0:
    ra = ["Discriminacion por raza en :",str(round((dis[0]*100)/sum,2))+"%"]
    vr.append(" ".join(ra))
    porce[0]=round((dis[0]*100)/sum)
    discrim.append("Raza")
  if dis[1]>0:
    ge = ["Discriminacion por Género en :",str(round((dis[1]*100)/sum,2))+"%"]
    vr.append(" ".join(ge))
    porce[1]=round((dis[1]*100)/sum)
    discrim.append("Genero")
  if dis[2]>0:
    ori = ["Discriminacion por Orientación Sexual en :",str(round((dis[2]*100)/sum,2))+"%"]
    vr.append(" ".join(ori))
    porce[2]=round((dis[2]*100)/sum)
    discrim.append("Orientacion Sexual")
  if dis[3]>0:
    ed = ["Discriminacion por Edad en :",str(round((dis[3]*100)/sum,2))+"%"]
    vr.append(" ".join(ed))
    porce[3]=round((dis[3]*100)/sum)
    discrim.append("Edad")
  if sum==0:
    vr.append("El texto no tiene ningun tipo de discriminación")
    
    discrim.append("Nada")
  
  print(porce)
  return "\n".join(vr),porce, discrim