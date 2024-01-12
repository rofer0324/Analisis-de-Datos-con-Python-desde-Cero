"""try:
    print(5/1)
except:
    print("...Hubo un error...")
finally:
    print("Siempre se ejecutara haya o no error.")"""
    

try:
    print(5/0)
except ZeroDivisionError as error_division:
    print(f"...Ha ocurrido el error: => {error_division}")
finally:
    print("siempre se ejecutara haya o no error.... MIJUA")
    
    