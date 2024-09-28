class AdminService:
    def __init__(self, poll_repository):
        self.poll_repository = poll_repository

    def create_poll(self, poll_name, candidates):
        # Logic to create a new poll with a set of candidates
        poll_id = self.poll_repository.create_new_poll(poll_name, candidates)
        return {"message": f"Poll '{poll_name}' created successfully.", "poll_id": poll_id}

    def close_poll(self, poll_id):
        # Logic to close a poll
        self.poll_repository.close_poll(poll_id)
        return {"message": f"Poll with ID '{poll_id}' has been closed."}
