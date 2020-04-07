if __name__ == "__main__":
  import re
  ciclo = True
  print ("Introduzca una cedula: ")
  while ciclo == True:
    ced = input()
    ##x = re.search("[1-9NE|PE]{1,2}[-][0-9]{1,4}[-][0-9]{1,5}$", ced)
    ##print (x.span())
    if re.search("^([1-9NE]|PE)[-][0-9]{1,4}[-][0-9]{1,5}$", ced):
      print ("CEDULA VALIDA")
      ciclo = False
    else :
      print ("CEDULA INVALIDA")
      print ("Por favor introduzca su cédula: ") 
