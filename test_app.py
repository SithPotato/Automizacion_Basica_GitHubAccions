from app import login

# CP-01
def test_login_exitoso():
    res = login("admin", "1234")
    assert res["success"] == True
    assert res["message"] == "Acceso concedido"

# CP-02
def test_usuario_vacio():
    res = login("", "1234")
    assert res["success"] == False
    assert res["message"] == "Usuario y contraseña son requeridos"

# CP-03
def test_contrasena_vacia():
    res = login("admin", "")
    assert res["success"] == False
    assert res["message"] == "Usuario y contraseña son requeridos"

# CP-04
def test_usuario_inexistente():
    res = login("pedro", "1234")
    assert res["success"] == False
    assert res["message"] == "Usuario no existe"

# CP-05
def test_contrasena_incorrecta():
    res = login("admin", "9999")
    assert res["success"] == False
    assert res["message"] == "Contraseña incorrecta"

# CP-06
def test_tiempo_respuesta():
    res = login("admin", "1234")
    assert res["response_time_ms"] > 0
    assert res["response_time_ms"] < 1000  # razonable

# CP-07
def test_estructura():
    res = login("admin", "1234")
    assert "success" in res
    assert "message" in res
    assert "response_time_ms" in res

# 🔍 PRUEBAS EXPLORATORIAS

def test_espacios_blanco():
    res = login(" admin ", "1234")
    assert res["success"] == False

def test_mayusculas():
    res = login("ADMIN", "1234")
    assert res["success"] == False

def test_caracteres_especiales():
    res = login("admin$", "1234")
    assert res["success"] == False

def test_ambos_vacios():
    res = login("", "")
    assert res["success"] == False

def test_contrasena_con_espacios():
    res = login("admin", " 1234 ")
    assert res["success"] == False