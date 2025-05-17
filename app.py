from flask import Flask, render_template, jsonify,request
from datetime import datetime
import json

app = Flask(__name__)

@app.route('/')
def home():
    with open('posts.json', 'r') as f:
        posts = json.load(f) 

    
    return render_template('index.html', posts=posts)

@app.route('/posts')
def get_posts():
    try:
        # فتح ملف JSON وقراءة البيانات
        with open('posts.json', 'r') as f:
            posts = json.load(f)
        return jsonify(posts)  # إرجاع البيانات بتنسيق JSON
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404


 
 
@app.route('/add-post', methods=['POST'])
def add_post():
    new_post = request.get_json()
    new_post['date'] = datetime.now().strftime('%d/%m/%Y - %H:%M')

    with open('posts.json', 'r', encoding='utf-8') as f:
        posts = json.load(f)

    posts.insert(0, new_post)

    with open('posts.json', 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False, indent=4)

    return jsonify({"status": "success"}), 200


if __name__ == '__main__':
    app.run(debug=True)