if __name__ == "__main__":
  print ("Introduzca un nombre: ")
  x = True
  y = 0
  while x == True:
    erro = ''
    nombre = input ()
    largo = int(len(nombre))
    for y in range(largo):
      letra = nombre[y]
      if letra.isdigit():
        ##print ("El nombre no puede tener caracteres numericos")
        erro = 'error'
        y = y + 1
    if erro == 'error':
     ##if nombre.isdigit():
      ##print (nombre.isalpha())
      print ("El nombre no debe contener digitos")
      print ("Por favor introduzca su nombre: ")
    elif largo <= 1:
        print ("Error.  Debe introducir un Nombre mayor a 1 caracter!")
    else:
        print ("Gracias por introducir un Nombre")
        print ("El nombre que introdujo fue: ", nombre)
        x = False
  

