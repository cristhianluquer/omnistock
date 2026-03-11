#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("🚀 Iniciando OmniStock...")

try:
    from flask import Flask, jsonify
    from app.config import get_db
    import platform

    app = Flask(__name__)

    @app.route('/')
    def home():
        return jsonify({"message": " OmniStock API funcionando", "status": "En linea"})

    @app.route('/health')
    def health():
        try:
            conn = get_db()
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES")
            return jsonify({"status": "healthy", "tables": cursor.fetchone()[0]})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    if __name__ == '__main__':
        print("🌐 Servidor: http://localhost:5001")
        app.run(host='0.0.0.0', port=5001, debug=True)
        
except ImportError as e:
    print(f"❌ Instala Flask: pip install flask")
    sys.exit(1)
