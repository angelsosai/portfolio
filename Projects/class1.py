# ¡usemos constantes!
FACTOR_MARTE = 0.378

def main():
    # Técnicamente el peso se mide en newtons, pero uno de tus
    # objetivos es enfocarte en Python, ¡no en la física!
    peso_tierra_str = input('Digite su peso en la Tierra: ')

    # input() devuelve un valor en forma de cadena, float obtiene el número
    peso_tierra = float(peso_tierra_str)

    # Usemos una variable más, es algo bueno cuando estás empezando a aprender
    peso_marte = peso_tierra * FACTOR_MARTE

    # ¡Nota la concatenación de cadenas!
    print('Su peso equivalente en Marte es: ' + str(peso_marte))

if __name__ == '__main__':
    main()
    
# python Variables.py main



#int 1,2,3,4,5

#float 1.0,2.0,3.0,4.0,5.0

#string "uno","dos","tres","cuatro","cinco"

#boolean True, False

#dictionary {"uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5}

#tuple ("uno", "dos", "tres", "cuatro", "cinco")

#list ["uno", "dos", "tres", "cuatro", "cinco"]

#set {"uno", "dos", "tres", "cuatro", "cinco"}