#!/bin/bash

# Menjalankan perintah gunicorn
gunicorn main:app --bind 0.0.0.0:$PORT &

# Menunggu gunicorn selesai memulai server
sleep 5

# Menjalankan perintah npm run build
npm run build
