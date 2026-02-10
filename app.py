from flask import Flask, render_template, request, redirect, url_for, jsonify, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from database import conectar_database
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/agenda")
def agenda():
    return render_template("agenda.html")

@app.route("/documentos")
def documentos():
    return render_template("documentalizar.html")

@app.route("/listas")
def listas():
    return render_template("lista.html")

@app.route("/perfil")
def perfil():
    return render_template("perfil.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/api/cadastro", methods=["POST"])
def api_cadastro():
    try:
        data = request.get_json()
        nome = data.get("nome")
        email = data.get("email")
        telefone = data.get("telefone")
        semana = data.get("semana_gestacional")
        senha = generate_password_hash(data.get("senha"))

        conn = conectar_database()
        if not conn:
            return jsonify({"message": "Erro ao conectar no banco de dados"}), 500

        cursor = conn.cursor()
        
        cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
        if cursor.fetchone():
            cursor.close()
            conn.close()
            return jsonify({"message": "Email já cadastrado"}), 400

        cursor.execute("""
            INSERT INTO users (nome, email, senha, telefone, semana_gestacional)
            VALUES (%s, %s, %s, %s, %s)
        """, (nome, email, senha, telefone, semana))

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"message": "Cadastro realizado com sucesso!"}), 200
    except Exception as e:
        return jsonify({"message": f"Erro: {str(e)}"}), 500

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/api/login", methods=["POST"])
def api_login():
    try:
        data = request.get_json()
        email = data.get("email")
        senha = data.get("senha")

        conn = conectar_database()
        if not conn:
            return jsonify({"message": "Erro ao conectar no banco de dados"}), 500

        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if not user or not check_password_hash(user["senha"], senha):
            return jsonify({"message": "Email ou senha incorretos"}), 401

        return jsonify({"message": "Login realizado com sucesso!", "user": {"nome": user["nome"], "email": user["email"]}}), 200
    except Exception as e:
        return jsonify({"message": f"Erro: {str(e)}"}), 500

@app.route("/api/upload", methods=["POST"])
def api_upload():
    try:
        if 'file' not in request.files:
            return jsonify({"message": "Nenhum arquivo enviado"}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({"message": "Arquivo vazio"}), 400
        
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        tipo = request.form.get('tipo', 'Outros')
        
        return jsonify({
            "message": "Upload realizado com sucesso",
            "filename": filename,
            "tipo": tipo,
            "url": f"/uploads/{filename}"
        }), 200
    except Exception as e:
        return jsonify({"message": f"Erro: {str(e)}"}), 500

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)
