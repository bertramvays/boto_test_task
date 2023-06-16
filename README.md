# Кейс 4 -Тестовое задание на позицию стажера Junior Backend Developer 

    Описание работы алгоритма скрипта.



    Алгоритм работы программы построен на основе переменной **couter**. Которая ведет учёт позитивных и негативных ситуаций в программе. Позитивное это когда слово в сообщении находит совпадение в словаре. Негативное когда слово повторяется несколько раз или в слове находиться несвойственное для руского языка сочетание букв или англоязычные символы(вынесены в список **non_typical_pattern**. Поиск осуществляется с помощью импортированого модуля **re**). 
    Принцип увелечения и уменшения переменной **couter** выбран для того, чтобы при получении сообщения которое имеет опечатки в тексте не забраковать его полностью. Изначально **couter** имеет значение 0, если планируеться использовать скрипт для обработки сообщений которые имеют более 4-5 слов целесообразно начальное значение задавать >0.
    С помощью списка **non_useful** скрипт очищает полученное сообщение от цифр и знаков припинания. Одновременно происходит выравнивание сообщения в нижний регистр.
    После очистки сообщения, оно разбиваеться на слова, точнее по частям выделенным в самостоятельные единицы (т.н. токены).
Токены которые состоят из 1 или 2 букв игнорируються, из-за того, что в большинстве своем не несут смысловой нагрузки.
    И на последок, токены из полученного сообщения сравниваються со словарем.  В качестве словаря я выбрал доступный для скачивания частотный список (униграмму) русского разговорного языка на сайте: opencorpora.org. Дополнительно в словарь были добавленны несколько десятков сленговых и жаргонных слов. В общей сложности, рабочий словарь насчитывает 166745 слов. Указанный словарь находится в файле **unigrams**. Этап проверки по словарю - осуществляеться на фильном этапе обработки полученного сообщения. Т.к. программа для каждого токена осуществляет перебор словаря.
    
  В самом конце скрипт, на основе количества позитивных и негативных событий, выводит свое мнение. Если было много ощибок, опечаток - белиберда. Если смысловых слов было больше - нет.
