usuarios = {
        "iperurena": {
            "nombre": "Iñaki",
            "apellido": "Perurena",
            "contraseña": "123123"
    },
        "fmuguruza": {
            "nombre": "Fermín",
            "apellido": "Muguruza",
            "contraseña": "654321"
    },
        "aolaizola": {
            "nombre": "Aimar",
            "apellido": "Olaizola",
            "contraseña": "123456"
    }
 }
usuario = input("Escriba su usuario: ")    
contraseña = input("Escriba su contraseña: ") 
intentos = 3

while(usuario not in usuarios.keys() or contraseña != usuarios[usuario]["contraseña"]):
    intentos = intentos - 1
    print(f"Acceso fallido, te quedan {intentos} intentos")

    usuario = input("Escriba su usuario: ") 
    contraseña = input("Escriba su contraseña: ")
    if intentos == 0:
        print("Cuenta bloqueada, no hay mas intentos ")
        break 
if usuario in usuarios.keys() and contraseña == usuarios[usuario]["contraseña"]:
    print({"nombre", "apellido"})