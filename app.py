from flask import Flask

# Initialize the Flask app
app = Flask(__jiraaveerappagari__)

# Define a route
@app.route("/")
def home():
    return "Hello, World! This is my first Flask app."

# Run the app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

