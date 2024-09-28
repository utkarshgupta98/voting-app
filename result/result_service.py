class ResultService:
    def __init__(self, result_repository):
        self.result_repository = result_repository

    def calculate_results(self):
        # Fetch results from the repository
        results = self.result_repository.get_results()
        total_votes = sum(results.values())
        
        # Calculate percentages
        percentage_results = {candidate: (votes / total_votes) * 100 for candidate, votes in results.items()}
        
        # Return results with percentages
        return percentage_results
