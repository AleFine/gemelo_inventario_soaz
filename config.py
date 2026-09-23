# config.py — Configuración global del Gemelo Digital de Inventario SOAZ
"""
Configuración de entorno. Los parámetros del MODELO no viven aquí: viven en
modulo_simulacion/parametros.py, con su procedencia declarada. Aquí solo va lo
que cambia entre máquinas y despliegues.
"""
import os

# === IDENTIDAD ===
NOMBRE_SISTEMA = "Gemelo Digital de Inventario — Comercializadora SOAZ"
INSTITUCION = "Universidad Nacional de Trujillo — Ingeniería de Sistemas"

# === FUENTE DE MOVIMIENTOS ===
# "sintetico" : el motor genera el histórico (modo actual, mientras el sistema
#               web de la tesis no esté operativo)
# "postgres"  : lee la tabla movimiento_inventario del sistema real
FUENTE_DATOS = os.getenv("FUENTE_DATOS", "sintetico")

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PUERTO", "5432"),
    "dbname": os.getenv("DB_NOMBRE", "soaz_inventarios"),
    "user": os.getenv("DB_USUARIO", "postgres"),
    "password": os.getenv("DB_CONTRASENA", ""),
}

# Cada cuántos minutos el servicio de sincronización lee movimientos nuevos.
MINUTOS_SINCRONIZACION = int(os.getenv("MINUTOS_SINCRONIZACION", 15))

# === PRESENTACIÓN ===
IDIOMA = os.getenv("IDIOMA", "es")
DECIMALES_MONEDA = 2

# === COPILOTO DE ESCENARIOS ===
# Traduce una pregunta del negocio en español a un escenario del motor. Es un
# módulo OPCIONAL: sin clave de API la pestaña se desactiva sola y las otras
# siete no se enteran. Nunca debe ser un requisito para correr el gemelo.
#
# El modelo se declara aquí, y no dentro del módulo, para poder cambiar de
# proveedor sin tocar código: basta exportar COPILOTO_MODELO.
COPILOTO_MODELO = os.getenv("COPILOTO_MODELO", "anthropic:claude-sonnet-5")

# Apagado manual, para sustentar sin red aunque la clave esté configurada.
COPILOTO_ACTIVO = os.getenv("COPILOTO_ACTIVO", "1") not in ("0", "false", "False")

# Profundidad de razonamiento: "low", "medium" o "high". Es el reemplazo moderno
# de `temperature`, que los modelos Claude 4.7 en adelante ya no aceptan (ver
# modulo_copiloto/proveedor.py). Sin declarar no se envía nada y manda el
# default del modelo, que es lo más seguro: un parámetro que el modelo no
# soporta devuelve 400 y tumba la pestaña entera.
COPILOTO_ESFUERZO = os.getenv("COPILOTO_ESFUERZO", "").strip().lower() or None
