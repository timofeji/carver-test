from flask import Blueprint, jsonify, render_template

from src.models import ISSLocation


location_blueprint = Blueprint('location', __name__, template_folder='./templates')


@location_blueprint.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html', isslocations=ISSLocation.query.all())


@location_blueprint.route('/locations', methods=['GET'])
def get_all_locations():
    res = {
        'status': 'success',
        'data': {
            'locations': [isslocation.to_json() for isslocation in ISSLocation.query.all()]
        }
    }
    return jsonify(res);
