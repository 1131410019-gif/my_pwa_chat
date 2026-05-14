from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Preset mood options
MOOD_LIST = ["😊 Happy", "🔥 Productive", "🚀 Focused", "☕ Chilling", "😴 Tired"]

# This list stays in memory while the server is running
posts = [
    {
        "username": "Pythonista",
        "avatar": "https://api.dicebear.com/7.x/adventurer/svg?seed=Python",
        "text": "Importing antigravity... I'm literally flying right now!",
        "likes": 42,
        "mood": "🚀 Focused"
    },
    {
        "username": "Gemini",
        "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=Gemini",
        "text": "The PWA manifests are all set. Ready to install!",
        "likes": 15,
        "mood": "😊 Happy"
    }
]

@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/board')
def board():
    # Pass both posts and moods to the HTML
    return render_template('board.html', posts=posts, moods=MOOD_LIST)

@app.route('/add_post', methods=['POST'])
def add_post():
    new_text = request.form.get('content')
    new_mood = request.form.get('mood')
    
    if new_text:
        # Adds the new post to the beginning of the list
        posts.insert(0, {
            "username": "Me",
            "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=Me",
            "text": new_text,
            "likes": 0,
            "mood": new_mood
        })
    return redirect(url_for('board'))

@app.route('/settings')
def settings():
    return render_template('settings.html')

if __name__ == '__main__':
    # host='0.0.0.0' allows you to view the app on your phone if it's on the same Wi-Fi!
    app.run(debug=True, host='0.0.0.0', port=5000)