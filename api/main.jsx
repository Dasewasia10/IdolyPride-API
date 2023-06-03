import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom';

function App() {
  const [cards, setCards] = useState([]);
  const [idols, setIdols] = useState([]);

  useEffect(() => {
    fetch('/api/card')
      .then((response) => response.json())
      .then((data) => setCards(data));

    fetch('/api/idol')
      .then((response) => response.json())
      .then((data) => setIdols(data));
  }, []);

  const handleAddCard = () => {
    const newCard = { /* Data kartu baru */ };
    fetch('/api/card', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(newCard),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.message === 'card added successfully') {
          // Card berhasil ditambahkan, lakukan sesuatu
        }
      });
  };

  const handleDeleteCard = (id) => {
    fetch(`/api/card/${id}`, { method: 'DELETE' })
      .then((response) => response.json())
      .then((data) => {
        if (data.message === 'card deleted successfully') {
          // Card berhasil dihapus, lakukan sesuatu
        }
      });
  };

  // Render tampilan kartu dan idol
  return (
    <div>
      <h1>Card List</h1>
      {cards.map((card) => (
        <div key={card.id}>
          <p>{card.title}</p>
          <p>{card.description}</p>
          <button onClick={() => handleDeleteCard(card.id)}>Delete</button>
        </div>
      ))}
      <h1>Idol List</h1>
      {idols.map((idol) => (
        <div key={idol.id}>
          <p>{idol.name}</p>
          <p>{idol.age}</p>
        </div>
      ))}
      <button onClick={handleAddCard}>Add Card</button>
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));
