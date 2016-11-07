from flask import Flask
from flask import abort, jsonify, request
from handlers.response_objects import Item, User, Trade, Error
from handlers import user_handler
from handlers import item_handler
from handlers import trade_handler
from handlers.db_handler import DBHandler

# create the app instance
app = Flask(__name__)

# create the MySQL database handler instance
db_handler = DBHandler(app)

# these are all the mock API end points.

@app.route("/dummy/api/get_user/<int:user_id>", methods=["GET"])
def mock_get_user(user_id):
	# just a dummy value for now
	return make_dummy_user(user_id)

@app.route("/dummy/api/new_user", methods=["POST"])
def mock_new_user():
	# check for malformed json request
	if not request.json:
		abort(400)

	return jsonify(request.json)

@app.route("/dummy/api/update_user", methods=["PUT"])
def mock_update_user():
	# check for malformed json request
	if not request.json:
		abort(400)
	
	return jsonify(request.json)

@app.route("/dummy/api/delete_user/<int:user_id>", methods=["DELETE"])
def mock_delete_user(user_id):
	return make_dummy_user(user_id)

# mock API methods
def make_dummy_user(user_id):
	return jsonify(
		user_id=user_id,
		name="test_user" + str(user_id),
		photo="pretend_this_is_a_photo",
		zipcode=32,
		email="test_email" + str(user_id) + "@email.com")

# ---------------------------------------------------------------------
# --------------------------- API -------------------------------------
# ---------------------------------------------------------------------

@app.route("/api/get_user/<int:user_id>", methods=["GET"])
def get_user(user_id):
	# check for malformed request
	if user_id <= 0:
		abort(400, "<get_user> only accepts positive user IDs")
	
	
	
	abort(400, "<get_user> is not accessable right now, sorry dawg")
