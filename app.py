from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    # Отримуємо дані з форми
    Yurchuk = request.form.get('name1', '').strip()  # Отримуємо значення поля name1
Oksanka = request.form.get('name2', '').strip()  # Отримуємо значення поля name2

    if not Yurchuk or not Oksanka:
        return "Both names must be provided.", 400

    # Логіка перевірки
    if set(Yurchuk) & set(Oksanka):  # Якщо є спільні букви
        result = "LOVE"
    else:
        result = "Friends"

    return f"<h1>Result: {result}</h1>"
