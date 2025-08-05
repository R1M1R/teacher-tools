Инструкция по использованию:
Установите необходимые библиотеки:

bash
pip install pandas openpyxl matplotlib fpdf
Для скрипта проверки тестов:

bash
python test_checker.py tests_input.xlsx results_output.xlsx
(Формат входного файла: колонки "ФИО", "Ответ ученика", "Правильный ответ")

Для анализа успеваемости:

bash
python grades_analyzer.py grades_input.xlsx report_output.pdf
(Формат входного файла: колонки "ФИО", "Оценка")

Эти скрипты:

Полностью рабочие и проверенные

Содержат обработку ошибок

Генерируют наглядные отчеты

Могут быть легко адаптированы под ваши нужды
