from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data for blog posts
blog_posts = [
    {"id": 1, "title": "Post 1", "content": "This is the content of the first post."},
    {"id": 2, "title": "Post 2", "content": "This is the content of the second post."},
]

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html', posts=blog_posts)

# Route to display a specific blog post
@app.route('/post/<int:post_id>')
def show_post(post_id):
    post = next((p for p in blog_posts if p['id'] == post_id), None)
    if post:
        return render_template('post.html', post=post)
    else:
        return "Post not found", 404

# Route to handle form submission for creating a new post
@app.route('/create_post', methods=['POST'])
def create_post():
    if request.method == 'POST':
        new_post = {
            "id": len(blog_posts) + 1,
            "title": request.form['title'],
            "content": request.form['content']
        }
        blog_posts.append(new_post)
        return render_template('post.html', post=new_post)

# Route that returns JSON data
@app.route('/api/posts', methods=['GET'])
def get_posts_json():
    return jsonify(blog_posts)
