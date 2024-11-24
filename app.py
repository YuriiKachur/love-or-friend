from flask import Flask, request, render_template

app = Flask(__name__)

# Головна сторінка з формою
@app.route('/')
def home():
    return render_template('index.html')

# Обробка форми
@app.route('/result', methods=['POST'])
def result():
    name1 = request.form['name1'].lower()
    name2 = request.form['name2'].lower()

    # Умова для перевірки
    if set(Yurchuk) & set(Oksasnka):  # Якщо є спільні букви
        result = "LOVE"
    else:
        result = "Friends"

    return f"<h1>Result: {result}</h1><br><a href='/'>Go back</a>"

if __name__ == '__main__':
    app.run(debug=True)
