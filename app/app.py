from flask import Flask
import socket
import os

app = Flask(__name__)
counter = 0

# Mapeamento de cores por APP_NAME
label_colors = {
    "App 1": "#FF5733",  # Vermelho
    "App 2": "#33B5FF",  # Azul
    "App 3": "#75FF33",  # Verde
    "App 4": "#C833FF"   # Roxo
}

@app.route('/')
def index():
    global counter
    counter += 1

    app_name = os.environ.get("APP_NAME", "Desconhecido")
    color = label_colors.get(app_name, "#AAAAAA")
    hostname = socket.gethostname()

    html = f"""
    <html>
        <head>
            <title>{app_name}</title>
            <style>
                body {{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    background-color: #f0f0f0;
                    font-family: Arial, sans-serif;
                }}
                .card {{
                    background-color: {color};
                    padding: 50px 80px;
                    border-radius: 20px;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                    text-align: center;
                    color: #fff;
                }}
                h1 {{
                    margin: 0 0 20px 0;
                    font-size: 32px;
                }}
                p {{
                    font-size: 20px;
                    margin: 5px 0;
                }}
            </style>
        </head>
        <body>
            <div class="card">
                <h1>{app_name}</h1>
                <p><strong>Container ID:</strong> {hostname}</p>
                <p><strong>Requisições:</strong> {counter}</p>
            </div>
        </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
