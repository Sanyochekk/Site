from random import randint
from flask import Flask, session, redirect, url_for, request, render_template
def index():
   max_quiz = 3
   session['quiz'] = randint(1, max_quiz)

   session['last_question'] = 0
   return render_template('main.html')
# f'''<a href="/test">Тест №{session['quiz']}</a>'''



def test():
   if request.method == 'POST':
      obj = request.form.to_dict(flat=False)
      return render_template('answer.html', obj=obj)
   return 'Получил не POST запрос'

def result():
   return "that's all folks!"



# Створюємо об'єкт веб-програми:
app = Flask(__name__)  
app.add_url_rule('/', 'index', index)   # створює правило для URL '/'
app.add_url_rule('/test', 'test', test, methods=['POST']) # створює правило для URL '/test'
app.add_url_rule('/result', 'result', result) # створює правило для URL '/test'
app.config['SECRET_KEY'] = 'secret_key'

if __name__ == '__main__':
   # Запускаємо веб-сервер:
   app.run(debug=True)
