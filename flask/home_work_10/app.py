from utils import get_candidates, get_candidate_id, get_candidate_skills

from flask import Flask

app = Flask(__name__)

@app.route('/')
def page_main():
    '''Главная страница'''

    candidate = get_candidates()
    return candidate

@app.route('/candidate/<int:id>/')
def page_candidate(id):
    '''Профиль кандидата'''

    candidate_id = get_candidate_id(id)
    return candidate_id

@app.route('/skills/<skill>/')
def page_skills(skill):
    '''Навыки кандидата'''

    candidates_skills = get_candidate_skills(skill)
    if len(candidates_skills) > 0:
        result = '<pre>'
        for candidate in candidates_skills:
            result += f"""
                        Имя кандидата: {candidate['name']}\n
                        Позиция кандидата: {candidate['position']}\n
                        Навыки кандидата: {candidate['skills']}\n
                    """
        result += '</pre>'

        return result
    else:
        return f"Кандидата с такими навыками нет"


app.run()