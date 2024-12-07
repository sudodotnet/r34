from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    image_folder = os.path.join(app.static_folder, 'images')
    images = [f'images/{img}' for img in os.listdir(image_folder) if img.lower().endswith(('png', 'jpg', 'jpeg', 'gif'))]

    per_page = 20
    total_pages = (len(images) + per_page - 1) // per_page
    # Изменяем здесь: уменьшаем page на 1, чтобы внутри приложения индекс начинался с 0
    page = int(request.args.get('page', 1)) - 1

    start = page * per_page
    end = start + per_page
    images_to_display = images[start:end]

    # Передаем функции max и min в контекст шаблона
    return render_template('index.html', images=images_to_display, total_pages=total_pages, current_page=page + 1, max=max, min=min)

if __name__ == '__main__':
    app.run(debug=True)