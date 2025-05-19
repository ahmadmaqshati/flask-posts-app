from flask import Flask, render_template, jsonify, request
from datetime import datetime
import json
import os

# Initialize the Flask app
app = Flask(__name__)




# الكلاس اللي طلبته
class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.date = datetime.now().strftime('%d/%m/%Y - %I:%M %p')
        self.id = None  # راح نحدده بعدين

    def to_dict(self):
        return {
            "content": self.content,
            "author": self.author,
            "date": self.date,
            "id": self.id
        }






# Route for the home page, rendering posts from a JSON file
@app.route('/')
def home():
    with open('posts.json', 'r') as f:
        posts = json.load(f)  # Load posts from the JSON file
    return render_template('index.html', posts=posts)  # Pass posts to the template

# Route to retrieve posts as JSON
@app.route('/posts')
def get_posts():
    try:
        with open('posts.json', 'r') as f:
            posts = json.load(f)
        return jsonify(posts)  # Return posts in JSON format
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404  # Handle file not found error

# Route to add a new post
@app.route('/add-post', methods=['POST'])
def add_post():
    new_post = request.get_json()  # Get post data from request
    new_post['date'] = datetime.now().strftime('%d/%m/%Y - %I:%M %p')  # Format the date

    # Load existing posts
    with open('posts.json', 'r', encoding='utf-8') as f:
        posts = json.load(f)

    # Generate a unique ID for the new post
    if posts:
        max_id = max(post.get('id', 0) for post in posts)
        new_post['id'] = max_id + 1
    else:
        new_post['id'] = 1

    posts.insert(0, new_post)  # Add the new post at the beginning

    # Save the updated posts list back to the file
    with open('posts.json', 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False, indent=4)

    return jsonify({"status": "success"}), 200 

# Route to delete a post by ID
@app.route('/delete-post/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    try:
        with open('posts.json', 'r', encoding='utf-8') as f:
            posts = json.load(f)

        # Filter out the post with the given ID
        posts = [post for post in posts if post.get('id') != post_id]

        with open('posts.json', 'w', encoding='utf-8') as f:
            json.dump(posts, f, ensure_ascii=False, indent=4)

        return jsonify({"status": "deleted"}), 200  
    except Exception as e:
        return jsonify({"error": str(e)}), 500  

# Route for user signup
@app.route('/signup', methods=['POST'])
def signup():
    user = request.get_json()
    
    users_file = os.path.join(os.path.dirname(__file__), 'users.json')

    # Load existing users, handling potential file errors
    if os.path.exists(users_file):
        with open(users_file, 'r', encoding='utf-8') as f:
            try:
                users = json.load(f)
            except json.JSONDecodeError:
                users = []
    else:
        users = []

    # Check if the username or email already exists
    for u in users:
        if u['username'] == user['username'] or u['name'] == user['name']:
            return jsonify({
                "status": "error", 
                "message": "Username or email already exists"
            }), 400

    print("إضافة المستخدم:", user)  

    users.append(user)  # Add the new user

    # Save updated user data
    with open(users_file, 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False, indent=4)

    print("تم الحفظ بنجاح في users.json") 

    return jsonify({"status": "success"}), 200 

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Load existing users
    with open('users.json', 'r', encoding='utf-8') as f:
        users = json.load(f)

    print("المستخدمين الموجودين حالياً:", users)  # Debug print

    # Verify username and password
    for user in users:
        if user['username'] == username and user['password'] == password:
            return jsonify({'status': 'success', 'user': user})

    return jsonify({'status': 'fail', 'message': 'اسم المستخدم أو كلمة المرور غير صحيحة'})  

# Run the Flask application in debug mode   
@app.route('/profile')
def profile():
    return render_template('profile.html')





if __name__ == '__main__':
    app.run(debug=True)