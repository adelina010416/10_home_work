import json


def load_candidates():
    """Загружает данные из файла candidates.json"""
    with open('candidates.json', 'r', encoding='utf-8') as file:
        candidates_list = json.load(file)
        return candidates_list


def get_all():
    """Возвращает список всех кандидатов"""
    return load_candidates()


def get_by_pk(pk):
    """Возвращает кандидата по номеру его пк"""
    candidates = get_all()
    for candidate in candidates:
        if candidate["pk"] == pk:
            return candidate


def get_by_skill(skill_name):
    """Возвращает список кандидатов по искомому навыку"""
    pk_list = set([])
    result = []
    skill_name = skill_name.lower()
    candidates = get_all()
    for candidate in candidates:
        skills = candidate["skills"].split(", ")
        for skill in skills:
            skill = skill.lower()
            if skill_name == skill:
                pk_list.add(candidate["pk"])
    [result.append(i) for i in candidates if i["pk"] in pk_list]
    return result

