import requests

def create_study_plan(subjects, days, hours):

    prompt = f"""
You are an AI study planner.

Create a study plan with the following details:

Subjects: {subjects}
Days until exam: {days}
Study hours per day: {hours}

Generate a day-by-day schedule including revision sessions.
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