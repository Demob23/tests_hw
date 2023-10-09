def return_sorted_list():
    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]

    filtered_logs = []

    for log in geo_logs:
        for key, value in log.items():
            if "Россия" in value:
                filtered_logs.append(f"{key}: {value}")

    print(f"Необходимые визиты: {filtered_logs}")


def print_unique_ids():
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}

    unique_ids = set()

    for key in ids:
        for item in ids[key]:
            unique_ids.add(item)

    print(f"Уникальные id: {unique_ids}")


def get_distribution():
    queries = [
        'кремниевая долина'
        'vk',
        'ютуб',
        'смотреть сериалы онлайн',
        'новости спорта',
        'афиша кино',
        'курс доллара',
        'сериалы этим летом',
        'курс по питону',
        'сериалы про спорт',
        'кремниевая долина смотреть онлайн',
        'кремниевая долина смотреть онлайн бесплатно'
    ]
    for element in set(len(querie.split()) for querie in queries):
        print(f"Для {element}: {len([word for word in queries if len(word.split()) == element]) / len(queries) :.2%}")


def return_channel_name():
    stats = {'facebook': 99, 'yandex': 120, 'vk': 40, 'google': 121, 'email': 555, 'ok': 98}
    name = ""
    maximum = max(stats.values())
    for title, content in stats.items():
        if content == maximum:
            name = title

    return f"Название канала с наибольшим объемом продаж: {name}"


def divide_tasks():
    print("#" * 40)


if __name__ == "__main__":
    return_sorted_list()
    divide_tasks()
    print_unique_ids()
    divide_tasks()
    get_distribution()
    divide_tasks()
    return_channel_name()
