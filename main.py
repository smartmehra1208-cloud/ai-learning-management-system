import requests
import json

class TestAnalyzer:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.example.com/analyze"  # Replace with actual API endpoint
        
    def analyze_score(self, score):
        """
        Analyze the test score and recommend a playlist based on the score range
        """
        if not (0 <= score <= 100):
            raise ValueError("Score must be between 0 and 100")
        
        # Determine playlist based on score range
        if 0 <= score < 20:
            playlist = "Playlist 1 (Beginner)"
        elif 20 <= score < 40:
            playlist = "Playlist 2 (Elementary)"
        elif 40 <= score < 60:
            playlist = "Playlist 3 (Intermediate)"
        elif 60 <= score < 80:
            playlist = "Playlist 4 (Advanced)"
        else:  # 80-100
            playlist = "Playlist 5 (Expert)"
        
        return playlist
    
    def get_detailed_analysis(self, score, subject="General"):
        """
        Get detailed analysis from the API using the provided key
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "score": score,
            "subject": subject,
            "model": "score_analyzer_v1"
        }
        
        try:
            # This is a mock API call - replace with actual API endpoint
            response = requests.post(self.base_url, headers=headers, json=payload, timeout=10)
            response.raise_for_status()
            
            # Parse the response
            analysis_data = response.json()
            return analysis_data
            
        except requests.exceptions.RequestException as e:
            # Fallback to local analysis if API is unavailable
            print(f"API request failed: {e}. Using local analysis.")
            return self._local_analysis(score, subject)
    
    def _local_analysis(self, score, subject):
        """
        Provide local analysis when API is unavailable
        """
        playlist = self.analyze_score(score)
        
        # Generate some mock analysis data
        analysis = {
            "score": score,
            "playlist_recommendation": playlist,
            "subject": subject,
            "strengths": self._get_strengths_based_on_score(score),
            "areas_for_improvement": self._get_improvement_areas_based_on_score(score),
            "next_steps": self._get_next_steps_based_on_score(score),
            "confidence_level": min(score / 2 + 50, 95)  # Mock confidence calculation
        }
        
        return analysis
    
    def _get_strengths_based_on_score(self, score):
        if score >= 80:
            return ["Strong foundational knowledge", "Excellent problem-solving skills", "High accuracy"]
        elif score >= 60:
            return ["Good understanding of concepts", "Solid application skills", "Consistent performance"]
        elif score >= 40:
            return ["Basic knowledge retention", "Partial understanding of key concepts"]
        else:
            return ["Willingness to learn", "Recognition of knowledge gaps"]
    
    def _get_improvement_areas_based_on_score(self, score):
        if score >= 80:
            return ["Advanced applications", "Complex problem scenarios"]
        elif score >= 60:
            return ["Conceptual depth", "Application in novel situations", "Time management"]
        elif score >= 40:
            return ["Fundamental concepts", "Basic application skills", "Practice needed"]
        else:
            return ["Basic foundational knowledge", "Core concept understanding", "Regular practice"]
    
    def _get_next_steps_based_on_score(self, score):
        playlist = self.analyze_score(score)
        
        recommendations = {
            "Playlist 1 (Beginner)": [
                "Start with foundational concepts",
                "Focus on basic terminology and principles",
                "Practice with simple exercises daily"
            ],
            "Playlist 2 (Elementary)": [
                "Review basic concepts",
                "Begin applying knowledge to simple problems",
                "Build consistency in practice"
            ],
            "Playlist 3 (Intermediate)": [
                "Strengthen conceptual understanding",
                "Practice with varied problem types",
                "Work on time management"
            ],
            "Playlist 4 (Advanced)": [
                "Tackle complex problems",
                "Focus on application in real-world scenarios",
                "Develop advanced strategies"
            ],
            "Playlist 5 (Expert)": [
                "Master nuanced applications",
                "Explore advanced topics beyond curriculum",
                "Consider mentoring others"
            ]
        }
        
        return recommendations[playlist]


# Example usage and test function
def main():
    # Initialize the analyzer with your API key
    analyzer = TestAnalyzer("85ceb0cb-53d0-458a-b4ee-4fe3a21565e1")
    
    # Test scores
    test_scores = [15, 32, 47, 65, 83, 92]
    
    print("Test Score Analysis Results")
    print("=" * 50)
    
    for score in test_scores:
        try:
            # Get analysis for each score
            analysis = analyzer.get_detailed_analysis(score, "Mathematics")
            
            # Display results
            print(f"\nScore: {score}/100")
            print(f"Playlist Recommendation: {analysis['playlist_recommendation']}")
            print(f"Subject: {analysis['subject']}")
            print("Strengths:")
            for strength in analysis['strengths']:
                print(f"  - {strength}")
            print("Areas for Improvement:")
            for area in analysis['areas_for_improvement']:
                print(f"  - {area}")
            print("Recommended Next Steps:")
            for step in analysis['next_steps']:
                print(f"  - {step}")
            print(f"Analysis Confidence: {analysis['confidence_level']:.1f}%")
            print("-" * 30)
            
        except ValueError as e:
            print(f"Error analyzing score {score}: {e}")


# Run the example if this script is executed directly
if __name__ == "__main__":
    main()