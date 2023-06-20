count = 0
#Primera pregunta
print("1. En donde se cria Luke?")
print("- Naboo")
print("- Tatooine")
print("- Jakku")
print("- Coruscant")
respuesta = input("Introduce tu respuesta: ")

respuesta_correcta1 = "tatooineTatooineTATOOINE"  #permite que se escriba en minuscula o en mayuscula
if respuesta in respuesta_correcta1:
    print("\U0001F603 Muy bien joven padawan, era Tatooine")
    count += 1
elif respuesta not in respuesta_correcta1: #Se puede abreviar haciendo solo un else y no elif
    print("\U0001F97A Oh, la respuesta correcta era Tatooine")

print() #Para separar las preguntas

#Segunda pregunta
print("2. En donde se cria Leia?")
print("- Naboo")
print("- Tatooine")
print("- Mustafar")
print("- Alderaan")
respuesta = input("Introduce tu respuesta: ")

respuesta_correcta2 = "alderaanAlderaanALDERAAN"
if respuesta in respuesta_correcta2:
    print("\U0001F603 Muy bien joven padawan, era Alderaan")
    count += 1
else:
    print("\U0001F97A Oh no, la respuesta correcta era Alderaan")

print()

#Tercera pregunta
print("3. En que planeta esta el Templo Jedi?")
print("- Naboo")
print("- Corellia")
print("- Coruscant")
print("- Endor")
respuesta = input("Introduce tu respuesta: ")

respuesta_correcta3 = "coruscantCoruscantCORUSCANT"
if respuesta in respuesta_correcta3:
    print("\U0001F603 Muy bien joven padawan, era Coruscant")
    count += 1
else:
    print("\U0001F97A Oh no, la respuesta correcta era Coruscant")

print()

#Cuarta pregunta
print("4. De que color es el sable de Mace Windu")
print("- Azul")
print("- Verde")
print("- Turquesa")
print("- Morado")
respuesta = input("Introduce tu respuesta: ")

respuesta_correcta4 = "moradoMoradoMORADO"
if respuesta in respuesta_correcta4:
    print("\U0001F603 Muy bien joven padawan, era Morado")
    count += 1
else:
    print("\U0001F97A Oh no, la respuesta correcta era Morado")

print()

#Quinta pregunta
print("5. Que personaje pensaba que la fuerza eran cuentos de viejas?")
print("- Anakin Skywalker")
print("- Luke Skywalker")
print("- Jar Jar Binks")
print("- Han Solo")
respuesta = input("Introduce tu respuesta: ")

respuesta_correcta5 = "han solo Han Solo HAN SOLO"
if respuesta in respuesta_correcta5:
    print("\U0001F603 Muy bien joven padawan, era Han Solo")
    count += 1
else:
    print("\U0001F97A Oh no, la respuesta correcta era Han Solo")

print()

#Sexta pregunta
print("6. Quien construyó a C-3PO?")
print("- Luke")
print("- Han Solo")
print("- Anakin")
print("- Los Jawas")
respuesta = input("Introduce tu respuesta: ")

respuesta_correcta6 = "anakinAnakinANAKIN"
if respuesta in respuesta_correcta6:
    print("\U0001F603 Muy bien joven padawan, era Anakin")
    count += 1
else:
    print("\U0001F97A Oh no, la respuesta correcta era Anakin")

print()

#Septima pregunta
print("7. De que estaba compuesto el bloque en el que congelaron a Han Solo?")
print("- Hielo")
print("- Monoxido de hidrogeno")
print("- Dilitio")
print("- Carbonita")
respuesta = input("Introduce tu respuesta: ")

respuesta_correcta7 = "carbonitaCarbonitaCARBONITA"
if respuesta in respuesta_correcta7:
    print("\U0001F603 Muy bien joven padawan, era de Carbonita")
    count += 1
else:
    print("\U0001F97A Oh no, la respuesta correcta era de Carbonita")

print()

#Octava pregunta
print("8. Que nos revelan que se esta construyendo al final de la Venganza de los Sith?")
print("- La base de la alianza rebelde")
print("- Un nuevo senado")
print("- Una estatua del emperador")
print("- La estrella de la muerte")
respuesta = input("Introduce tu respuesta: ")

respuesta_correcta8 = "la estrella de la muerte La estrella de la muerte LA ESTRELLA DE LA MUERTE"
if respuesta in respuesta_correcta8:
    print("\U0001F603 Muy bien joven padawan, era la estrella de la muerte")
    count += 1
else:
    print("\U0001F97A Oh no, la respuesta correcta era la estrella de la muerte")

print()

#Novena pregunta
print("9. Para que usaba Han Solo y Chewbacca el compartimento secreto del Halcon Milenario?")
print("- De despensa")
print("- Para transportar prisioneros")
print("- Para esconderse si la cosa se ponia fea")
print("- Para el contrabando")
respuesta = input("Introduce tu respuesta: ")

respuesta_correcta9 = "para el contrabando Para el contrabando PARA EL CONTRABANDO"
if respuesta in respuesta_correcta9:
    print("\U0001F603 Muy bien joven padawan, era para el contrabando")
    count += 1
else:
    print("\U0001F97A Oh no, la respuesta correcta era para el contrabando")

print()

#Decima pregunta
print("10. En que plantea se exilia Yoda?")
print("- Bespin")
print("- Tatooine")
print("- Dagobah")
print("- Geonosis")
respuesta = input("Introduce tu respuesta: ")

respuesta_correcta10 = "dagobahDagobahDAGOBAH"
if respuesta in respuesta_correcta10:
    print("\U0001F603 Muy bien joven padawan, era en Dagobah")
    count += 1
else:
    print("\U0001F97A Oh no, la respuesta correcta era en Dagobah")

print() 

if count == 9:
    print("\U0001F973", count, "/10 Te otorgamos el rango de Caballero Jedi", sep = "")
elif count == 10:
    print("\U0001F525", count, "/10 FELICIDADES eres un autentico Maestro Jedi", sep = "")
else:
    print("Tu puntuacion es: ", count, "/10", sep = "")
