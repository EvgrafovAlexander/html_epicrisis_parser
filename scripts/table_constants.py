TABLE_FINDER_DICT = {'Анализ инфекций': ['иммуноферментные исследования инфекций'],
                     'Анализ мочи общий': ['анализ мочи общий'],
                     'Биохимия Covid19': ['биохимия covid19'],
                     'Анализ крови биохимический': ['анализ крови биохимический'],
                     'Выявление антител к ВИЧ': ['выявления антител к вич'],
                     'Гликемический профиль': ['гликемический профиль'],
                     'Глюкоза в венозной крови': ['глюкоза в венозной крови'],
                     'Интерлейкин': ['интерлейкин'],
                     'Коагулограмма': ['ориентировочное исследование системы гемостаза'],
                     'Коагулограмма Covid19': ['коагулограмма covid19'],
                     'МР с КЛА': ['мр с кла'],
                     'ОАК Covid19': ['оак covid19'],
                     'Общий анализ крови развернутый': ['общий (клинический) анализ крови развернутый',
                                                        'анализ крови развернутый'],
                     'Общий анализ мокроты': ['общий анализ мокроты'],
                     'Общий (клинический) анализ мочи': ['общий (клинический) анализ мочи',
                                                         'анализ мочи'],
                     'ПЦР': ['определение рнк коронавируса торс'],
                     'Уровень тропонинов': ['исследование уровня тропонинов'],
                     'Уровень ферритина': ['исследование уровня ферритина'],
                     'Кислотно-основное равновесие': ['кислотно-основного равновесия']
                     }


MEDICATIONS_TABLE = {
    'id': {'name': 'id', 'type': '', 'unit': []},
    'абактал': {'name': 'id', 'type': '', 'unit': ['абактал']},
    'азитромицин': {'name': 'id', 'type': '', 'unit': ['азитромицин']},
    'амброксол': {'name': 'id', 'type': '', 'unit': ['амброксол']},
    'апиксабан': {'name': 'id', 'type': '', 'unit': ['апиксабан']},
    'арбидол': {'name': 'id', 'type': '', 'unit': ['арбидол']},
    'бромгексин': {'name': 'id', 'type': '', 'unit': ['бромгексин']},
    'дексаметазон': {'name': 'id', 'type': '', 'unit': ['дексаметазон']},
    'доксициклин': {'name': 'id', 'type': '', 'unit': ['доксициклин']},
    'ибуклин': {'name': 'id', 'type': '', 'unit': ['ибуклин']},
    'ингаверин': {'name': 'id', 'type': '', 'unit': ['ингаверин']},
    'кагоцел': {'name': 'id', 'type': '', 'unit': ['кагоцел']},
    'ксарелто': {'name': 'id', 'type': '', 'unit': ['ксарелто']},
    'левофлоксацин': {'name': 'id', 'type': '', 'unit': ['левофлоксацин']},
    'лизиноприл': {'name': 'id', 'type': '', 'unit': ['лизиноприл']},
    'нурофен': {'name': 'id', 'type': '', 'unit': ['нурофен']},
    'оксигенотерапия': {'name': 'id', 'type': '', 'unit': ['оксигенотерапия']},
    'осельтамивир': {'name': 'id', 'type': '', 'unit': ['осельтамивир']},
    'панцеф': {'name': 'id', 'type': '', 'unit': ['панцеф']},
    'парацетамол': {'name': 'id', 'type': '', 'unit': ['парацетамол']},
    'полиоксидоний': {'name': 'id', 'type': '', 'unit': ['полиоксидоний']},
    'рениколд': {'name': 'id', 'type': '', 'unit': ['рениколд']},
    'рулид': {'name': 'id', 'type': '', 'unit': ['рулид']},
    'солютаб': {'name': 'id', 'type': '', 'unit': ['солютаб']},
    'флемоксин': {'name': 'id', 'type': '', 'unit': ['флемоксин']},
    'цефтриаксон': {'name': 'id', 'type': '', 'unit': ['цефтриаксон']},
    'эниксум': {'name': 'id', 'type': '', 'unit': ['эниксум']},
}

COLUMN_TABLE = {'Коагулограмма Covid19': ['date', 'PV', 'MNO', 'D_dimer'],
                'Общий анализ мочи': ['date', 'glykoza', 'belok', 'pH', 'ud_ves',
                                      'leikocits', 'blood', 'nitrits',
                                      'ketons', 'urobilinogen', 'bilirubin',
                                      'askorbin', 'color', 'transparency'],
                'ОАК Covid19': ['date', 'WBC', 'RBC', 'MCV', 'HCT', 'HGB', 'MCH',
                                'MCHC', 'PLT', 'MPV', 'PCT', 'PDW', 'RDW', 'RDWa',
                                'NEU_perc', 'LYM_perc', 'MON_perc', 'NEU', 'LYM',
                                'MON', 'SOE', 'glykoza', 'laktat', 'EOS_perc',
                                'BAS_perc', 'EOS', 'BAS', 'segmento_perc', 'eozino_perc',
                                'monocito_perc', 'limfocito_perc', 'palochko_perc'],
                'ПЦР': ['date', 'detected'],
                'Биохимия Covid19': ['CRE', 'ALT', 'AST', 'LDG', 'UREA', 'fosph_act',
                                     'KFK', 'Albumin', 'TBil', 'SRB', 'K', 'Na', 'glykoza']
                }

TABLE_DICT = {
    'Основная информация':
        {
            'id': {'name': 'id', 'type': '', 'unit': []},
            'имя': {'name': 'Имя', 'type': '', 'unit': []},
            'фамилия': {'name': 'Фамилия', 'type': '', 'unit': []},
            'отчество': {'name': 'Отчество', 'type': '', 'unit': []},
            'пол': {'name': 'Пол', 'type': '', 'unit': []},
            'dob': {'name': 'Дата рождения', 'type': '', 'unit': []},
            'treatment_start': {'name': 'Дата поступления', 'type': '', 'unit': []},
            'treatment_stop': {'name': 'Дата выписки', 'type': '', 'unit': []},
            'start_disease_date': {'name': 'Дата начала заболевания', 'type': '', 'unit': []},
            'perc_of_defeat': {'name': 'Процент поражения', 'type': '', 'unit': []},
            'base': {'name': 'Основной диагноз', 'type': '', 'unit': []},
            'identified': {'name': 'Обнаружен вирус', 'type': '', 'unit': []},
            'form': {'name': 'Степень тяжести', 'type': '', 'unit': []},
            'complication': {'name': 'Осложнения', 'type': '', 'unit': []},
            'respiratory_distress': {'name': 'Дыхательная недостаточность', 'type': '', 'unit': []},
            'is_concomitant_disease': {'name': 'Сопутствующие заболевания', 'type': '', 'unit': []},
            'conc_dieases_text': {'name': 'Перечень соп. заболеваний', 'type': '', 'unit': []},
            'is_weakness': {'name': 'Слабость', 'type': '', 'unit': []},
            'is_aches': {'name': 'Кашель', 'type': '', 'unit': []},
            'is_dyspnea_at_rest': {'name': 'Одышка в покое', 'type': '', 'unit': []},
            'is_dyspnea_at_stress': {'name': 'Одышка при нагрузке', 'type': '', 'unit': []},
        },
    'Коагулограмма':
        {
            'id': {'name': 'id', 'type': '', 'unit': []},
            'дата': {'name': 'Дата', 'type': 'date', 'unit': ['']},
            'аптв': {'name': 'АПТВ', 'type': 'float', 'unit': ['(сек.)']},
            'мно': {'name': 'МНО', 'type': 'float', 'unit': ['']},
            'пв': {'name': 'ПВ', 'type': 'float', 'unit': ['(сек.)']},
            'пти': {'name': 'ПТИ', 'type': 'float', 'unit': ['(%)']},
            'фибриноген': {'name': 'Фибриноген', 'type': 'float', 'unit': ['(г/л)', '(г/дл)', '(g/l)']},
            'inn ddi': {'name': 'INN Ddi', 'type': 'float', 'unit': ['(мг/л)']}
        },
    'Общий анализ крови развернутый':
        {
            'id': {'name': 'id', 'type': '', 'unit': []},
            'дата': {'name': 'Дата', 'type': 'date', 'unit': ['']},
            'эритроциты': {'name': 'Эритроциты', 'type': 'float', 'unit': ['(10deg12)']},
            'тромбоциты': {'name': 'Тромбоциты', 'type': 'float', 'unit': ['(10deg9)', '(10 в 9 ст. /л)']},
            'нейтрофилы': {'name': 'Нейтрофилы', 'type': 'float', 'unit': ['(%)']},
            'моноциты': {'name': 'Моноциты', 'type': 'float', 'unit': ['(%)']},
            'лимфоциты': {'name': 'Лимфоциты', 'type': 'float', 'unit': ['(%)']},
            'лейкоциты': {'name': 'Лейкоциты', 'type': 'float', 'unit': ['(10deg9)', '(10 в 9 ст. /л)']},
            'гемоглобин': {'name': 'Гемоглобин', 'type': 'float', 'unit': ['(г/л)', '(г/дл)', '(g/l)']},
            'гематокрит': {'name': 'Гематокрит', 'type': 'float', 'unit': ['(%)']},
            'mcv': {'name': 'MCV', 'type': 'float', 'unit': ['(фл)', '(fl)']},
            'mch': {'name': 'MCH', 'type': 'float', 'unit': ['(пг)', '(pg)']},
            'mchc': {'name': 'MCHC', 'type': 'float', 'unit': ['(г/л)', '(г/дл)', '(g/l)']},
            'mpv': {'name': 'MPV', 'type': 'float', 'unit': ['(фл)', '(fl)']},
            'эозинофилы': {'name': 'Эозинофилы', 'type': 'float', 'unit': ['(%)']},
            'базофилы': {'name': 'Базофилы', 'type': 'float', 'unit': ['(%)']},
            'rdw-sd': {'name': 'RDW-SD', 'type': 'float', 'unit': ['(фл)', '(fl)']}
        },
    'Анализ крови биохимический':
        {
            'id': {'name': 'id', 'type': '', 'unit': []},
            'дата': {'name': 'Дата', 'type': 'date', 'unit': ['']},
            'алт': {'name': 'АЛТ', 'type': 'float', 'unit': ['(ед/л)']},
            'общий белок': {'name': 'Общий белок', 'type': 'float', 'unit': ['(г/л)', '(г/дл)', '(g/l)']},
            'мочевина': {'name': 'Мочевина', 'type': 'float', 'unit': ['(ммоль/л)']},
            'креатинин': {'name': 'Креатинин', 'type': 'float', 'unit': ['(мкмоль/л)']},
            'исследование уровня глюкозы в крови': {'name': 'Исследование уровня глюкозы в крови',
                                                    'type': 'float', 'unit': ['(ммоль/л)']},
            'аст': {'name': 'АСТ', 'type': 'float', 'unit': ['(ед/л)']},
            'ферритин': {'name': 'Ферритин', 'type': 'float', 'unit': ['(нг/мл)']},
            'общий билирубин': {'name': 'Общий билирубин', 'type': 'float', 'unit': ['(мкмоль/л)']},
            'общий холестерин': {'name': 'Общий холестерин', 'type': 'float', 'unit': ['(ммоль/л)']},
            'глюкоза': {'name': 'Глюкоза', 'type': 'float', 'unit': ['(ммоль/л)']},
            'срб': {'name': 'СРБ', 'type': 'float', 'unit': ['(мг/л)']}
        },
    # TODO - Таблица не доделана
    'Общий (клинический) анализ мочи':
        {
            'id': {'name': 'id', 'type': '', 'unit': []},
            'дата': {'name': 'Дата', 'type': 'date', 'unit': ['']},
            'цвет': {'name': 'Цвет', 'type': 'class', 'unit': {'светло-желтый': ['светло-желтый', 'с/желтый'],
                                                               'соломено-желтый': ['соломено-желтый']}},
            'ph кислотность': {'name': 'pH', 'type': 'class', 'unit': {'кис': ['кис'],
                                                                       'нейтр': ['нейтр']}},
            'удельного веса': {'name': 'Определение удельного веса (относительной плотности) мочи',
                                           'type': 'class', 'unit': {'м\м': ['м\м']}},
            'определение белка в моче': {'name': 'Определение белка в моче',
                                         'type': 'class', 'unit': {'отр': ['отр']}},
            'leu': {'name': 'LEU', 'type': 'not', 'unit': {}},
            'bld': {'name': 'BLD', 'type': 'not', 'unit': {}},
            'фосфаты': {'name': 'Фосфаты', 'type': 'not', 'unit': {}},
            'плоский эпителий': {'name': 'Плоский эпителий', 'type': 'not', 'unit': {}},
            'почечный эпителий': {'name': 'Почечный эпителий', 'type': 'not', 'unit': {}},
            'оксалаты': {'name': 'Оксалаты', 'type': 'not', 'unit': {}}
        },
    'Кислотно-основное равновесие':
        {
            'id': {'name': 'id', 'type': '', 'unit': []},
            'дата': {'name': 'Дата', 'type': 'date', 'unit': ['']},
            'к+': {'name': 'Калий', 'type': 'float', 'unit': ['(ммоль/л)']},
            'na+': {'name': 'Натрий', 'type': 'float', 'unit': ['(ммоль/л)']}
        },
    'Перед госпитализацией': MEDICATIONS_TABLE.copy(),
    'Во время госпитализации': MEDICATIONS_TABLE.copy(),
    'После госпитализации': MEDICATIONS_TABLE.copy()
}
