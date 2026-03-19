# Proyecto Login Testing

## Descripción
Función de login con validaciones básicas y suite completa de pruebas con pytest.

## Estructura
```
PythonApp/
├── app.py              # Lógica de login
├── test_app.py         # Suite de pruebas
├── requirements.txt    # Dependencias
└── .github/workflows/pytest.yml  # GitHub Actions CI
```

## Casos de prueba

### CP-01 a CP-07 (Base)
| ID    | Descripción               |
|-------|---------------------------|
| CP-01 | Login exitoso             |
| CP-02 | Usuario vacío             |
| CP-03 | Contraseña vacía          |
| CP-04 | Usuario inexistente       |
| CP-05 | Contraseña incorrecta     |
| CP-06 | Tiempo de respuesta razonable |
| CP-07 | Estructura del response   |

### Pruebas Exploratorias
| ID     | Descripción                      |
|--------|----------------------------------|
| EXP-01 | Espacios en blanco               |
| EXP-02 | Mayúsculas en usuario            |
| EXP-03 | Caracteres especiales            |
| EXP-04 | Ambos campos vacíos              |
| EXP-05 | Contraseña con espacios          |

## Ejecutar pruebas
```bash
pip install -r requirements.txt
pytest test_app.py -v
```
