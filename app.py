from flask import Flask, render_template, redirect
from controllers.links_controller import links_bp

app = Flask(__name__)
app.register_blueprint(links_bp)

if __name__ == '__main__':
    app.run(debug=True)