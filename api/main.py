from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os

app = Flask(__name__)
cors = CORS(app, resources={
    r"/api/*": {"origins": ["https://idoly-pride-api.vercel.app", "http://localhost:5173", "https://idolyp.vercel.app"]}
})

## CARD
# Membaca file JSON 
with open('card.json', 'r') as file:
    card = json.load(file)

# Route dengan metode GET
@app.route('/api/card', methods=['GET'])
def get_all_card():
    return jsonify(card)

# Route dengan metode GET
@app.route('/api/card/<int:id>', methods=['GET'])
def get_card(id):
    for item in card:
        if item['id'] == id:
            return jsonify(item)

    return jsonify({"message": "card not found"})

# Route dengan metode GET
@app.route('/api/card/name/<name>', methods=['GET'])
def get_cards_by_name(name):
    # Mengubah underscore menjadi spasi
    name_with_spaces = name.replace("_", " ")

    cards = []
    reversed_name = " ".join(reversed(name_with_spaces.split(" ")))
    # Mencari idol berdasarkan nama asli
    for item in card:
        if item['name'].lower() == name_with_spaces.lower():
            cards.append(item)
        elif item['name'].lower().startswith(name_with_spaces.lower()) or item['name'].lower() == reversed_name.lower():
            cards.append(item)
    
    if cards:
        return jsonify(cards)
    else:
        return jsonify({"message": "idol not found"})

# Route dengan metode GET
@app.route('/api/card/type/<type>', methods=['GET'])
def get_cards_by_type(type):
    cards = []
    # Mencari card berdasarkan type
    for item in card:
        if item['type'].lower() == type.lower():
            cards.append(item)
    
    if cards:
        return jsonify(cards)
    else:
        return jsonify({"message": "idol not found"})

# Route dengan metode GET
@app.route('/api/card/ability/<ability>', methods=['GET'])
def get_cards_by_ability(ability):
    cards = []
    # Mencari card berdasarkan type
    for item in card:
        if item['ability'].lower() == ability.lower():
            cards.append(item)
    
    if cards:
        return jsonify(cards)
    else:
        return jsonify({"message": "idol not found"})

# Route dengan metode POST
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
with open('idol.json', 'r') as file:
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

# Route dengan metode GET
@app.route('/api/idol/<string:_id>', methods=['GET'])
def get_idol_by__id(_id):
    for item in idol:
        if item['_id'] == _id:
            return jsonify(item)

    return jsonify({"message": "card not found"})

# Route dengan metode GET
@app.route('/api/idol/name/<name>', methods=['GET'])
def get_idol_by_name(name):
    # Mengubah underscore menjadi spasi
    name_with_spaces = name.replace("_", " ")

    # Mencari idol berdasarkan nama asli
    for item in idol:
        if item['name'] == name_with_spaces:
            return jsonify(item)

        # Mencari idol berdasarkan nama asli atau nama yang sudah dibalik (case insensitive)
        reversed_name = " ".join(reversed(name_with_spaces.split(" ")))
        if item['name'].lower().startswith(name_with_spaces.lower()) or item['name'].lower() == reversed_name.lower():
            return jsonify(item)

    return jsonify({"message": "idol not found"})

# Route dengan metode GET
@app.route('/api/idol/group/<group>', methods=['GET'])
def get_idols_by_group(group):
    # Mengubah underscore menjadi spasi
    group_with_spaces = group.replace("_", " ")

    idols = []
    # Mencari idol berdasarkan group
    for item in idol:
        if 'detail' in item and item['detail'][0]['group'].lower() == group_with_spaces.lower():
            idols.append(item)

    if idols:
        return jsonify(idols)
    else:
        return jsonify({"message": "idols not found"})


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

# Fungsi untuk memastikan api memang sudah berjalan
@app.route('/api/', methods=['GET'])
def api():
    return jsonify({'message': 'API is running'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))