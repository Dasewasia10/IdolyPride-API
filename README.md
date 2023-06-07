# IdolyPride API

This is a Flask-based API for managing card and idol data for the Idoly Pride project. The API provides endpoints to retrieve, add, update, and delete card and idol information.

NOTICE : <span style="color:red">**Data Card is still on search and collection missions. Please be patient**</span>

## Disclaimer

Please note that all data provided by this API is subject to copyright by [QualiArts](https://qualiarts.jp/) and not by [Dasewasia10](https://github.com/Dasewasia10), the owner of this repository. The API is solely intended for educational and non-commercial purposes.

## Getting Started

To get started with the API, follow the instructions below.

### Prerequisites

- Python 3.x
- Flask

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Dasewasia10/IdolyPride-API.git
   ```

Note: It's recommended to use venv as environment. See [venv](https://docs.python.org/3/library/venv.html) for more details.

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Use `cd` to go to folder where API function located

   ```bash
   cd api
   ```

2. Start the Flask server:

   ```bash
   python main.py
   ```

3. The API will be accessible at `http://localhost:5000`.

### Endpoints

#### Card 
<span style="color:red">**API data still on searching mission. Please be patient.**</span>

- `GET /api/card`: Get all cards.
- `GET /api/card/<int:id>`: Get a card by ID.
- `POST /api/card`: Add a new card.
- `PUT /api/card/<int:id>`: Update a card by ID.
- `DELETE /api/card/<int:id>`: Delete a card by ID.

#### Idol

- `GET /api/idol`: Get all idols.
- `GET /api/idol/<int:id>`: Get an idol by ID. Example: `GET /api/card/1`
  ```json
  {
    "id": 1,
    "name": "Sakura Kawasaki",
    ...
  }
  ```
- `GET /api/idol/name/<name>`: Get an idol by name (case-insensitive).
- `GET /api/idol/group/<group>`: Get idols by group (case-insensitive).
- `POST /api/idol`: Add a new idol.
- `PUT /api/idol/<int:id>`: Update an idol by ID.
- `DELETE /api/idol/<int:id>`: Delete an idol by ID.

#### API Status

- `GET /api/`: Check the status of the API.

### Examples

Here are some examples of how to use the API endpoints:

- Get all cards:

  ```bash
  GET /api/card
  ```

- Get a card by ID:

  ```bash
  GET /api/card/1
  ```

  Response:

  ```json
  {
    "id": 1,
    "name": "Sakura Kawasaki",
    ...
  }
  ```

- Add a new card:

  ```bash
  POST /api/card

  Body:
  {
    "id": 3,
    "name": "Card Name",
    ...
  }
  ```

- Update a card by ID:

  ```bash
  PUT /api/card/1

  Body:
  {
    "name": "Updated Card Name",
    ...
  }
  ```

- Delete a card by ID:
  ```bash
  DELETE /api/card/1
  ```

This a same go with idol.

### Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. Feel free to contact me.

### License

This project is licensed under the [MIT License](LICENSE).

### Acknowledgements

Special thanks to [Idoly Pride](https://idolypride.jp/) for providing the data used in this API.

```
