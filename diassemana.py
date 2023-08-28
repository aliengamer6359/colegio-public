dias_semana = input("que dia de la semana? ").lower()
if dias_semana == "lunes":
    mensaje = "Animo"
elif dias_semana == "martes":
    mensaje = "sigue adelante"
elif dias_semana == "miercoles":
    mensaje = "mitad de semana"
elif dias_semana == "jueves":
    mensaje = "ya falta poco"
elif dias_semana == "viernes":
    mensaje = "ultimo dia de trabajo de la semana"
elif dias_semana == "sabado":
    mensaje = "puedes descansar"
elif dias_semana == "domingo":
    mensaje = "toca llegar recargado al trabajo"
else:
    mensaje = "ese no es un dìa"
    

print(mensaje)