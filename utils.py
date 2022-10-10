import json


def load_candidates():
    """
    Функция загружает данные из json файла
    :return: возвращает список словарей
    """
    with open('candidates.json', 'r', encoding='utf-8') as file:
        data_list = json.load(file)
    return data_list


def get_all():
    """
    :return: Возвращает список словарей кондидатов
    """
    return load_candidates()


def get_by_pk(pk):
    """
    :param pk: номер кандидата
    :return: по номеру кандидата возвращает отдельный словарь кандидата
    """
    candidates = get_all()

    for candidate in candidates:
        if candidate['pk'] == pk:
            return candidate



def get_by_skill(skill_name):
    """

    :param skill_name: название навыков
    :return: по названию навыков возвращет спсиок кандидатов имеющих их
    """
    candidates = get_all()
    list_candidate = []
    for candidate in candidates:
        if skill_name.lower() in candidate['skills'].lower().split(', '):
            list_candidate.append(candidate)

    return list_candidate
