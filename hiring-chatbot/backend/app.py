from flask import Flask, request, jsonify
from routes import candidate_routes, cv_analysis_routes

app = Flask(__name__)

# Registering Routes
app.register_blueprint(candidate_routes, url_prefix='/candidate')
app.register_blueprint(cv_analysis_routes, url_prefix='/cv')

@app.route('/')
def home():
    return "Hiring Chatbot API"

if __name__ == '__main__':
    app.run(debug=True)
