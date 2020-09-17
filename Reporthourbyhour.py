#from datetime import date
import os
import datetime



def WelcomeToGeneratorReport():
    print('Generador de reportes hora x hora')
    print('Developed by Carlos A. Pérez Méndez')


def ClearScreen():
    Cleaner = os.system("cls")
    return Cleaner
    
def Date_and_Time ():
    today = datetime.datetime.now()
    return today
  

def Report_Generator(modelo, modelo_serial, nombre, nomina, turno, Date_Time):
  
    file_log  = open('path where the log is saved', 'a')  #This argument does not has the rigth path because you should configure it according with your directory.
    file_log.write("Fecha y hora: " + Date_Time + os.linesep)
    file_log.write("Modelo:" + modelo + os.linesep)
    file_log.write("Serial:"+ modelo_serial + os.linesep)
    file_log.write("Nombre:" + nombre + os.linesep)
    file_log.write("WD ID:" + nomina + os.linesep)
    file_log.write("Turno:" + turno + os.linesep)
    file_log.write("\n")
    file_log.close()
    ClearScreen()





def main():
    
     
    while True:
        
        print('Ingrese el modelo')
        modelo = input()
        print('Ingrese el serial')
        modelo_serial = input()
        print('Nombre')
        nombre = input()
        print('WD ID:')
        nomina = input()
        print('Turno')
        turno = input()
        Date_Time = Date_and_Time()
        Date_Time = str(Date_Time)
        Report_Generator(modelo, modelo_serial, nombre, nomina, turno, Date_Time)

    

       
         








if __name__ == '__main__':
    WelcomeToGeneratorReport()
    main()
        
