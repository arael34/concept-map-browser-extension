from flask import Blueprint, request, render_template, session, jsonify
# from backend.ml_pipeline import ml_pipeline

routes = Blueprint("routes", __name__)

# global variable to load models just once
# MODEL_DICT = ml_pipeline.get_loaded_model_dict()

@routes.route('/<id>')
def home_page(id):
    text = request.args.get('text')
    if text != None:
        session[id] = text
    if id in session:
        text = session[id]
    # parse text and call ml_pipeline.get_triples() here. 
    return render_template('index.html', id=id)

@routes.route('/test', methods=['GET', 'POST'])
def testfn():
    # GET request
    if request.method == 'GET':
        message = {'greeting':'Hello from Python'}
        return jsonify(message)  # serialize and use JSON headers
    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Success', 200

# @routes.route('/conceptmap', methods=['POST'])
# def get_triples_from_ml_backend():
#     input_text_dict = request.get_json(force=True)
#     triples = ml_pipeline.get_triples(input_text_dict['text'], MODEL_DICT)
#     print('\n\n\n')
#     print('##########################################################')
#     print(len(triples))
#     print('##########################################################')
#     print('\n\n\n')
#     return jsonify(triples)
