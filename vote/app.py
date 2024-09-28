from flask import Flask, request, jsonify
from vote.vote_service import VoteService
from result.result_service import ResultService
from admin.admin_service import AdminService

app = Flask(__name__)

# Initialize services (assuming repositories are already implemented and passed here)
vote_service = VoteService(vote_repository=None)  # Replace None with your actual repository
result_service = ResultService(result_repository=None)  # Replace None with your actual repository
admin_service = AdminService(poll_repository=None)  # Replace None with your actual repository

# Route for submitting a vote
@app.route('/vote', methods=['POST'])
def submit_vote():
    data = request.json
    user_id = data.get('user_id')
    candidate_id = data.get('candidate_id')

    try:
        result = vote_service.submit_vote(user_id, candidate_id)
        return jsonify(result), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

# Route for viewing the voting results
@app.route('/results', methods=['GET'])
def get_results():
    results = result_service.calculate_results()
    return jsonify(results), 200

# Route for creating a new poll (admin)
@app.route('/admin/create_poll', methods=['POST'])
def create_poll():
    data = request.json
    poll_name = data.get('poll_name')
    candidates = data.get('candidates')  # Expecting a list of candidates

    result = admin_service.create_poll(poll_name, candidates)
    return jsonify(result), 201

# Route for closing a poll (admin)
@app.route('/admin/close_poll/<poll_id>', methods=['POST'])
def close_poll(poll_id):
    result = admin_service.close_poll(poll_id)
    return jsonify(result), 200

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
