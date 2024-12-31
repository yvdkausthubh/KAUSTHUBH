from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/interview-questions')
def interview_questions():
    return render_template('interview_questions.html')

@app.route('/experiments')
def experiments():
    return render_template('experiments.html')

@app.route('/simulation-projects')
def simulation_projects():
    return render_template('simulation_projects.html')

@app.route('/articles')
def articles():
    return render_template('articles.html')

@app.route('/about')
def about():
    return render_template('about.html')  # Ensure you have an 'about.html' template

@app.route('/contact')
def contact():
    return render_template('contact.html')  # Ensure you have a 'contact.html' template

if __name__ == '__main__':
    app.run(debug=True)
