from tools.concept_explainer import explain_concept
from tools.quiz_generator import generate_quiz
from tools.study_planner import create_study_plan


def concept_agent(topic, level):
    return explain_concept(topic, level)


def quiz_agent(topic, difficulty):
    return generate_quiz(topic, difficulty)


def study_agent(subjects, days, hours):
    return create_study_plan(subjects, days, hours)