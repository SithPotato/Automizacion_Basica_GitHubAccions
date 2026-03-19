import time

def login(usuario, contraseña):
    inicio = time.time()

    # Validación campos vacíos
    if not usuario or not contraseña:
        return {
            "success": False,
            "message": "Usuario y contraseña son requeridos",
            "response_time_ms": int((time.time() - inicio) * 1000)
        }

    # Usuario válido
    if usuario != "admin":
        return {
            "success": False,
            "message": "Usuario no existe",
            "response_time_ms": int((time.time() - inicio) * 1000)
        }

    # Contraseña correcta
    if contraseña != "1234":
        return {
            "success": False,
            "message": "Contraseña incorrecta",
            "response_time_ms": int((time.time() - inicio) * 1000)
        }

    return {
        "success": True,
        "message": "Acceso concedido",
        "response_time_ms": int((time.time() - inicio) * 1000)
    }