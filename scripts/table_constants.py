TABLE_FINDER_DICT = {'Анализ инфекций': ['иммуноферментные исследования инфекций'],
                     'Биохимия Covid19': ['биохимия covid19'],
                     'Выявление антител к ВИЧ': ['выявления антител к вич'],
                     'Гликемический профиль': ['гликемический профиль'],
                     'Коагулограмма Covid19': ['коагулограмма covid19'],
                     'МР с КЛА': ['мр с кла'],
                     'ОАК Covid19': ['оак covid19'],
                     'Общий анализ крови развернутый': ['общий (клинический) анализ крови развернутый',
                                                        'анализ крови развернутый'],
                     'Общий анализ мокроты': ['общий анализ мокроты'],
                     'Общий анализ мочи': ['общий (клинический) анализ мочи',
                                           'анализ мочи'],
                     'ПЦР': ['определение рнк коронавируса торс'],
                     'Уровень ферритина': ['исследование уровня ферритина']
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