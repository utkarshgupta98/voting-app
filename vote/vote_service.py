class VoteService:
    def __init__(self, vote_repository):
        self.vote_repository = vote_repository

    def submit_vote(self, user_id, candidate_id):
        if not self.is_valid_candidate(candidate_id):
            raise ValueError("Invalid candidate selected.")
        if self.has_already_voted(user_id):
            raise ValueError("User has already voted.")
        
        # Process the vote
        self.vote_repository.save_vote(user_id, candidate_id)
        return {"message": "Vote submitted successfully", "selected_candidate": candidate_id}

    def is_valid_candidate(self, candidate_id):
        # Check if the candidate exists
        valid_candidates = self.vote_repository.get_all_candidates()
        return candidate_id in valid_candidates

    def has_already_voted(self, user_id):
        # Check if the user has already voted
        return self.vote_repository.user_has_voted(user_id)
