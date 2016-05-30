import xlrd

def checkPhrase(x):
  if  checkPhrase=="":
    return False
  for char in x:
    if char > u'\u9fa5' or char < u'\u4e00':
     return False
  return True
def checkBopomofo(x):
  if x=="":
    return False
  if x[0]>u'\u3129' or x[0] < u'\u3105':
    return False
  return True

book1 = xlrd.open_workbook("dict_revised_1.xls")
book2 = xlrd.open_workbook("dict_revised_2.xls")
book3 = xlrd.open_workbook("dict_revised_3.xls")
sh1 = book1.sheet_by_index(0)
sh2 = book2.sheet_by_index(0)
sh3 = book3.sheet_by_index(0)
f = open("dict_revised.json","w")
json = "{\n\"userphrase\": [\n"
for rx in range(1,sh1.nrows):
  data = sh1.row(rx)
  phrase = data[2].value
  bopomofo = data[6].value
  if checkPhrase(phrase) and checkBopomofo(bopomofo):  
    json+="{\n\"bopomofo\":\""+bopomofo.encode('utf-8')+"\",\n"
    json+="\"phrase\":\""+phrase.encode('utf-8')+"\"\n},\n"
for rx in range(1,sh2.nrows):
  data = sh2.row(rx)
  phrase = data[2].value
  bopomofo = data[6].value
  if checkPhrase(phrase) and checkBopomofo(bopomofo):
    json+="{\n\"bopomofo\":\""+bopomofo.encode('utf-8')+"\",\n"
    json+="\"phrase\":\""+phrase.encode('utf-8')+"\"\n},\n"
for rx in range(1,sh3.nrows):
  data = sh3.row(rx)
  phrase = data[2].value
  bopomofo = data[6].value
  if checkPhrase(phrase) and checkBopomofo(bopomofo):
    json+="{\n\"bopomofo\":\""+bopomofo.encode('utf-8')+"\",\n"
    json+="\"phrase\":\""+phrase.encode('utf-8')+"\"\n},\n"
json= json[:-2]
json+="\n]\n}"
f.write(json)
f.close 
