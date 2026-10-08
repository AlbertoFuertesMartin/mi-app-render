from flask import Flask
import socket
import datetime

# Creamos la aplicación web
app = Flask(__name__)

# Ruta principal
@app.route("/")
def home():
    return """
    <h1>¡Hola desde Render!</h1>
    <p>Esta aplicación Python se está ejecutando en la nube como un servicio PaaS.</p>
    <p>Alberto Fuertes y Ariel Santos</p>
    <p>Visita <a href="/status">/status</a> para ver información del servidor.</p>
    """

# Ruta secundaria /status
@app.route("/status")
def status():
    info = {
        "hora_actual": datetime.datetime.now().isoformat(),
        "servidor": socket.gethostname()
    }
    return info

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
