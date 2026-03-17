import requests

def generate_quiz(topic, difficulty):

    prompt = f"""
You are an AI teacher.

Create 5 multiple choice questions on the topic: {topic}

Difficulty level: {difficulty}

For each question include:
- Question
- 4 options
- Correct answer
- Short explanation
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