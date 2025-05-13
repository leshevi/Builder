from flask import Flask, render_template

app = Flask(__name__)

# Данные для портфолио
portfolio_data = {
    "name": "Иван Петров",
    "profession": "Строитель-отделочник",
    "experience": "15 лет",
    "services": [
        "Штукатурные работы",
        "Плиточные работы",
        "Поклейка обоев",
        "Напольные покрытия",
        "Малярные работы",
        "Установка сантехники"
    ],
    "projects": [
        {"title": "Ремонт квартиры 85 кв.м", "image": "project1.jpg",
         "description": "Полный цикл отделочных работ"},
        {"title": "Отделка офиса", "image": "project2.jpg",
         "description": "Плитка, покраска, натяжные потолки"},
        {"title": "Ванная комната под ключ", "image": "project3.jpg",
         "description": "Сантехника, плитка, электрика"}
    ],
    "contacts": {
        "phone": "+7 (123) 456-78-90",
        "email": "ivan.petrov@example.com",
        "address": "г. Москва"
    }
}

@app.route('/')
def index():
    return render_template('index.html', data=portfolio_data)

if __name__ == '__main__':
    app.run(debug=True)
