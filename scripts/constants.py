patient_id = 0

COLUMNS = ['id', 'first_name', 'second_name', 'middle_name', 'sex',
           'dob', 'treatment_start', 'treatment_stop',
           'base', 'identified', 'form', 'complication', 'respiratory_distress',
           'is_concomitant_disease', 'conc_dieases_text']

DIAG_DICT = {
             # основной диагноз
             'base':
                 {'COVID-19': ['коронавирусная инфекция',
                               'коронавирусная',
                               'covid-19']},
             'identified':
                 {'Вирус не идентифицирован': ['вирус не идентифицирован',
                                               'не идентифицирован'],
                  'Вирус идентифицирован': ['вирус идентифицирован',
                                            'идентифицирован']},
             'form':
                 {'Средне-тяжелая': ['средне-тяжелая форма',
                                     'средне -тяжелая форма',
                                     'средне-тяжелая'],
                  'Легкая': ['легкая форма',
                             'легкая']},
             # осложнения
             'complication':
                 {'Внебольничная двусторонняя полисегментарная пневмония':
                            ['внебольничная двусторонняя полисегментарная пневмония']}
             }


F_BASE_DIAG = [('основной', 'осложнение'),
               ('диагнозом', 'осложнение'),
               ('диагнозом', 'осл')]

F_COMP_DIAG = [('осложнение', 'сопутствующий'),
               ('осложнение', 'жалобы'),
               ('осл', 'жалобы'),
               ('осложнение', 'анамнез')]

F_CONC_DIAG = [('сопутствующий:', 'жалобы'),
               ('сопутствующие:', 'жалобы'),
               ('сопутствующий', 'жалобы'),
               ('сопутствующие', 'жалобы'),
               ('сопутствующее:', 'анамнез'),
               ('сопутствующий:', 'анамнез')]

F_COMPLAINTS = [('жалобы', 'анамнез')]

END_DIAG = ['жалобы', 'анамнез']

PATH = './Epicrises/'
