import requests

def explain_concept(topic, level):

    prompt = f"""
You are an AI tutor.

Teach the concept '{topic}' to a {level} student.

Return the response in this format:

CONCEPT:
Short definition

STEP-BY-STEP:
Explanation

EXAMPLE:
Real world example

QUIZ:
One short question
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "tinyllama",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]