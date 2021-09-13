



#internet version
def new_string(str):
  if len(str) >= 2 and str[:2] == "Is":
    return str
  return "Is" + str

print(new_string("Blynai yra"))
print(new_string("Is blynai good?"))