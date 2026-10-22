# Ejemplo mínimo división
linea = "     2026-10-12 08:15:22|INFO|auth_service|Usuario inicio sesion exitosamente.     "
print(linea)

linea_limpia=linea.strip()

campos = linea_limpia.split("|")

print(campos)

print(campos[1]) # Resultado: "ERROR"
print(len(campos)) # Resultado: 4
