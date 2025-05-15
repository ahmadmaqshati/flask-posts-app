from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    with open('posts.json', 'r') as f:
    #posts = json.load(f) 

      posts = [
        {
            "username": "ahmad",
            "user_image": "https://cdn-icons-png.flaticon.com/512/219/219986.png",
            "image": "https://media.istockphoto.com/id/165578655/photo/silhouette-of-a-girl-walking-over-the-beach-at-sunset.jpg?s=612x612&w=0&k=20&c=ZNV74AgqoMwOf0yfmbTnDDt5BIDUb7AZDgQJjU-yha8=",
            "date": "just now",
            "title": "My first post",
            "body": "This is my first post!",
            "comments_count": 2
        },
        {
            "username": "ali",
            "user_image": "https://example.com/user2.png",
            "image": "https://www.k12digest.com/wp-content/uploads/2024/03/1-3-550x330.jpg",
            "date": "10 min ago",
            "title": "Sunset 🌇",
            "body": "Beautiful view",
            "comments_count": 5
        },
        {
            "username": "hasan",
            "user_image": "https://example.com/user2.png",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLSY9QSR_rZ8AhtzsCn77ntJYF737nLwooAg&s",
            "date": "10 min ago",
            "title": "Sunset 🌇",
            "body": "Beautiful view",
            "comments_count": 5
        },
        {
            "username": "hasan",
            "user_image": "https://example.com/user2.png",
            "image": "https://cdn.img.sarabic.ae/img/103348/26/1033482628_0:125:3071:1861_1920x0_80_0_0_9a80046256c8ffc1989a271f78d53b91.jpg",
            "date": "10 min ago",
            "title": "Sunset 🌇",
            "body": "Beautiful view",
            "comments_count": 5
        },

        {
            "username": "hasan",
            "user_image": "https://example.com/user2.png",
            "image": "https://www.k12digest.com/wp-content/uploads/2024/03/1-3-550x330.jpg",
            "date": "10 min ago",
            "title": "Sunset 🌇",
            "body": "Beautiful view",
            "comments_count": 5
        },
        {
            "username": "hasan",
            "user_image": "https://example.com/user2.png",
            "image": "https://www.k12digest.com/wp-content/uploads/2024/03/1-3-550x330.jpg",
            "date": "10 min ago",
            "title": "Sunset 🌇",
            "body": "Beautiful view",
            "comments_count": 5
        },
         {
        "username": "sara",
        "user_image": "https://example.com/user3.png",
        "image": "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
        "date": "20 min ago",
        "title": "Nature Walk",
        "body": "A peaceful walk in the woods 🌲",
        "comments_count": 3
    },
    {
        "username": "mohammed",
        "user_image": "https://example.com/user4.png",
        "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
        "date": "30 min ago",
        "title": "Ocean vibes 🌊",
        "body": "Relaxing by the sea",
        "comments_count": 7
    },
    {
        "username": "laila",
        "user_image": "https://example.com/user5.png",
        "image": "https://images.unsplash.com/photo-1496389392040-1e6f02b49d90",
        "date": "1 hour ago",
        "title": "City Lights ✨",
        "body": "City at night is magical!",
        "comments_count": 4
    },
    {
        "username": "omar",
        "user_image": "https://example.com/user6.png",
        "image": "https://images.unsplash.com/photo-1470770841072-f978cf4d019e",
        "date": "2 hours ago",
        "title": "Mountain Adventure 🏔️",
        "body": "Hiking to new heights",
        "comments_count": 6
    },
    {
        "username": "fatima",
        "user_image": "https://example.com/user7.png",
        "image": "https://images.unsplash.com/photo-1488521787991-ed7bbaae773c",
        "date": "3 hours ago",
        "title": "Desert Beauty 🏜️",
        "body": "Golden sands and peaceful silence",
        "comments_count": 2
    },
    {
        "username": "yousef",
        "user_image": "https://example.com/user8.png",
        "image": "https://images.unsplash.com/photo-1469474968028-56623f02e42e",
        "date": "5 hours ago",
        "title": "Countryside Escape 🌾",
        "body": "Back to the roots",
        "comments_count": 1
    }

    ]
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

if __name__ == '__main__':
    app.run(debug=True)
 
 