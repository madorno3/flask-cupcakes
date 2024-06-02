from flask import Flask, request, jsonify, render_template

from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "secret"

app.app_context().push()
connect_db(app)

@app.route("/")
def home():
    cupcakes=Cupcake.query.all()
    return render_template("home.html", cupcakes=cupcakes)

@app.route("/api/cupcakes")
def cupcakes():
    cupcakes = [cupcake.to_dict() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)


@app.route("/api/cupcakes/<int:id>")
def single_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.to_dict())

# create cupcake route
@app.route("/api/cupcakes", methods=["POST"])
def make_cupcake():
    data = request.json
    
    cupcake = Cupcake(
        flavor=data['flavor'],
        rating=data['rating'],
        size=data['size'],
        image=data['image'] or None)

    db.session.add(cupcake)
    db.session.commit()
    return (jsonify(cupcake=cupcake.to_dict()), 201)

@app.route("/api/cupcakes/<int:id>", methods=["PATCH"])
def update_cupcake(id):
    
    data = request.json
    cupcake = Cupcake.query.get_or_404(id)

    cupcake.flavor = data['flavor']
    cupcake.rating = data['rating']
    cupcake.size = data['size']
    cupcake.image = data['image']

    db.session.add(cupcake)
    db.session.commit()

    return jsonify(cupcake=cupcake.to_dict())

@app.route("/api/cupcakes/<int:id>", methods=["DELETE"])
def delete_cupcake(id):
    
    cupcake = Cupcake.query.get_or_404(id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="deleted")

# questions to look up. when to use serialize. 
# when to use data = request.json




