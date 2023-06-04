from flask import Flask, jsonify, request
import json
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost:5000/idolyp'
db = SQLAlchemy(app)

## Model
class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    name = db.Column(db.String(255))
    jpname = db.Column(db.String(255))
    quote = db.Column(db.Text)
    type = db.Column(db.String(50))
    ability = db.Column(db.String(50))
    initial = db.Column(db.Integer)
    live_skill = db.Column(db.JSON)
    cheer = db.Column(db.JSON)
    image = db.Column(db.JSON)

class Idol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    jpname = db.Column(db.String(255))
    va = db.Column(db.String(255))
    description = db.Column(db.Text)
    detail = db.Column(db.JSON)
    image = db.Column(db.JSON)
    voice = db.Column(db.JSON)


## CARD
# Membaca file JSON 
with open('api/card.json', 'r') as file:
    card = json.load(file)

# Route dengan metode GET
@app.route('/api/card', methods=['GET'])
def get_all_card():
    cards = Card.query.all()
    result = []
    for card in cards:
        result.append({
            'id': card.id,
            'title': card.title,
            'name': card.name,
            'jpname': card.jpname,
            'quote': card.quote,
            'type': card.type,
            'ability': card.ability,
            'initial': card.initial,
            'live-skill': card.live_skill,
            'cheer': card.cheer,
            'image': card.image
        })
    return jsonify(result)


# Route dengan metode GET
@app.route('/api/card/<int:id>', methods=['GET'])
def get_card(id):
    for item in card:
        if item['id'] == id:
            return jsonify(item)

    return jsonify({"message": "card not found"})

@app.route('/api/card', methods=['POST'])
def add_card():
    new_card = request.get_json()  # Mendapatkan card baru dari body permintaan
    card.append(new_card)  # Menambahkan card baru ke dalam daftar card
    
    return jsonify({"message": "card added successfully"})

# Route dengan metode PUT untuk memperbarui card dengan ID tertentu
@app.route('/api/card/<int:id>', methods=['PUT'])
def update_card_card(id):
    # Menerima card baru dari body permintaan
    updated_card = request.get_json()

    # Mencari card dengan ID yang sesuai
    for item in card:
        if item['id'] == id:
            # Memperbarui card dengan card baru
            item.update(updated_card)
            return jsonify({'message': 'card updated successfully'})

    # Jika tidak ada card dengan ID yang sesuai
    return jsonify({'message': 'card not found'})

# Route dengan metode DELETE untuk menghapus card dengan ID tertentu
@app.route('/api/card/<int:id>', methods=['DELETE'])
def delete_card(id):
    # Mencari card dengan ID yang sesuai
    for index, item in enumerate(card):
        if item['id'] == id:
            # Menghapus card dengan ID yang sesuai
            del card[index]
            return jsonify({'message': 'card deleted successfully'})

    # Jika tidak ada card dengan ID yang sesuai
    return jsonify({'message': 'card not found'})

## IDOL
# Membaca file JSON 
with open('api/idol.json', 'r') as file:
    idol = json.load(file)

# Route dengan metode GET 
@app.route('/api/idol', methods=['GET'])
def get_all_idol():
    
    return jsonify(idol)

# Route dengan metode GET
@app.route('/api/idol/<int:id>', methods=['GET'])
def get_idol(id):
    for item in idol:
        if item['id'] == id:
            return jsonify(item)

    return jsonify({"message": "idol not found"})

@app.route('/api/idol', methods=['POST'])
def add_idol():
    new_idol = request.get_json()  # Mendapatkan idol baru dari body permintaan
    idol.append(new_idol)  # Menambahkan idol baru ke dalam daftar idol
    
    return jsonify({"message": "idol added successfully"})

# Route dengan metode PUT untuk memperbarui idol dengan ID tertentu
@app.route('/api/idol/<int:id>', methods=['PUT'])
def update_idol_idol(id):
    # Menerima idol baru dari body permintaan
    updated_idol = request.get_json()

    # Mencari idol dengan ID yang sesuai
    for item in idol:
        if item['id'] == id:
            # Memperbarui idol dengan idol baru
            item.update(updated_idol)
            return jsonify({'message': 'idol updated successfully'})

    # Jika tidak ada idol dengan ID yang sesuai
    return jsonify({'message': 'idol not found'})

# Route dengan metode DELETE untuk menghapus idol dengan ID tertentu
@app.route('/api/idol/<int:id>', methods=['DELETE'])
def delete_idol(id):
    # Mencari idol dengan ID yang sesuai
    for index, item in enumerate(idol):
        if item['id'] == id:
            # Menghapus idol dengan ID yang sesuai
            del idol[index]
            return jsonify({'message': 'idol deleted successfully'})

    # Jika tidak ada idol dengan ID yang sesuai
    return jsonify({'message': 'idol not found'})

# Route untuk menangani permintaan API dari React
@app.route('/api', methods=['GET'])
def api():
    return jsonify({'message': 'API is running'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))