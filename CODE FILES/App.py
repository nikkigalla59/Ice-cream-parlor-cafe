from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ice_cream_parlor.db"
db = SQLAlchemy(app)

class Flavor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    seasonal = db.Column(db.Boolean, default=False)

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

class CustomerSuggestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    suggestion = db.Column(db.String(200), nullable=False)

class Allergen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"))
    flavor_id = db.Column(db.Integer, db.ForeignKey("flavor.id"))
    quantity = db.Column(db.Integer, nullable=False)

@app.route("/")
def index():
    flavors = Flavor.query.all()
    return render_template("index.html", flavors=flavors)

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q")
    flavors = Flavor.query.filter(Flavor.name.like("%" + query + "%")).all()
    return render_template("search.html", flavors=flavors)

@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    flavor_id = request.form["flavor_id"]
    quantity = request.form["quantity"]
    cart_item = CartItem(flavor_id=flavor_id, quantity=quantity)
    db.session.add(cart_item)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/suggest_flavor", methods=["POST"])
def suggest_flavor():
    name = request.form["name"]
    email = request.form["email"]
    suggestion = request.form["suggestion"]
    customer_suggestion = CustomerSuggestion(name=name, email=email, suggestion=suggestion)
    db.session.add(customer_suggestion)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/add_allergen", methods=["POST"])
def add_allergen():
    name = request.form["name"]
    allergen = Allergen.query.filter_by(name=name).first()
    if not allergen:
        allergen = Allergen(name=name)
        db.session.add(allergen)
        db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)