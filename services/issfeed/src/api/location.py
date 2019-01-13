from flask import Blueprint, jsonify, render_template

from src.models import ISSLocation


location_blueprint = Blueprint('location', __name__, template_folder='./templates')


@location_blueprint.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', isslocations=ISSLocation.query.all())


@location_blueprint.route('/swaggerspec', methods=['GET', 'POST'])
def swaggerspec():
    return render_template('swaggerspec.html')


@location_blueprint.route('/locations', methods=['GET'])
def get_all_locations():
    res = {
        'status': 'success',
        'data': {
            'locations': [isslocation.to_json() for isslocation in ISSLocation.query.all()]
        }
    }
    return jsonify(res), 200


@location_blueprint.route('/location/<timestamp>', methods=['GET'])
def get_location(timestamp):
    try:
        location = ISSLocation.query.filter_by(timestamp=int(timestamp)).first()
        if not location:
           raise Exception('Location record could not be found') 
        else:
            res = {
                'status': 'success',
                'data': {
                    'locations': location.to_json()
                }
            }
            return jsonify(res), 200

    except Exception as err:
        res = {
                'status': 'fail',
                'message':  err.args
        }
        return jsonify(res), 404




