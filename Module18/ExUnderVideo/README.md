## Задание под видео lesson №1
Задача 1. Заказ

После того, как человек сделал заказ в интернет-магазине, ему на почту приходит оповещение с его именем и номером заказа.

Напишите программу, которая получает на вход имя и код заказа, а затем выводит на экран соответствующее сообщение. Для решения используйте строковый метод format.



Пример:

Имя: Иван

Номер заказа: 10948



Здравствуйте, Иван! Ваш номер заказа: 10948. Приятного дня!



Задача 2. Долги

Один наш друг занял у нас определённую сумму денег и всё никак не может их вернуть. А деньги нам нужны. Поэтому мы решили написать небольшой скрипт-напоминалку, который, возможно, разбудит его совесть.

Напишите программу, которая получает на вход имя и долг, а затем выводит на экран сообщение, где имя повторяется несколько раз (и долг, возможно, тоже). Используйте числа в названиях ключей.



Пример:

Введите имя: Том

Введите долг: 100

Том! Том, привет! Как дела, Том? Где мои 100 рублей? Том! 



Задача 3. IP-адрес

IP-адрес компьютера состоит из 4 чисел, разделённых точкой. Каждое число находится в диапазоне от 0 до 255 (включительно). 



Пример правильного адреса: 192.168.1.0

Пример неправильного адреса: 192.168.300.0



Напишите программу, которая получает на вход 4 числа и выводит на экран IP-адрес. Используйте переменную ip_address в качестве шаблона. Обеспечьте контроль ввода.
## Задание под видео lesson №2
Задача 1. Улучшенная лингвистика 2

Усовершенствуйте старую программу:  

У нас есть список из трёх слов, которые вводит пользователь. Затем вводится сам текст произведения, который вводится уже в одну строку. Напишите программу, которая посчитает, сколько раз слова пользователя встречаются в тексте. 



Задача 2. Бабушка

У одной бабушки, когда та переписывается с внуком, постоянно залипает кнопка пробела. В итоге между словами получаются огромные расстояния. Внук не знает как это поправить в самом телефоне, поэтому обратился к вам за помощью.

Пользователь вводит строку. Напишите программу, которая преобразовывает в этой строке все идущие подряд пробелы в один и выводит результат на экран.



Пример:

Введите текст: У       нас         пошёл                    снег    !     



Исправленный текст: У нас пошёл снег !



Задача 3. Разделители символов

Человек хочет сделать рассылку поздравлений для определённого списка людей. Поздравления для разных людей он хочет написать по-разному. 



Напишите программу, которая запрашивает у пользователя: 

Шаблон поздравления (туда вставляется ФИ и возраст)

ФИ людей (в одну строку, разделяются запятой)

Возраст каждого человека (в одну строку через пробел)

В конце  программа выводит поздравления и всех именинников в одну строку вместе с их возрастом.



Пример:

Введите шаблон поздравления, в шаблоне можно использовать конструкцию {name} и {age}: С днём рождения, {name}! С {age}-летием тебя!

Список людей через запятую: Иван Иванов, Петя Петров, Лена Ленова

Возраст людей через пробел: 20 30 18



С днём рождения, Иван Иванов! С 20-летием тебя!

С днём рождения, Петя Петров! С 30-летием тебя!

С днём рождения, Лена Ленова! С 18-летием тебя!



Именинники: Иван Иванов 20, Петя Петров 30, Лена Ленова 18
## Задание под видео lesson №3
Задача 1. Шифр Цезаря 2

Мы уже писали программу, которая шифрует строку с помощью шифра Цезаря. Напомним, что в таком способе шифрования каждая буква заменяется на следующую по алфавиту через K позиций по кругу. 

Напишите (модифицируйте) программу, которая реализует этот алгоритм шифрования. Не используйте конкатенацию и сделайте так, чтобы текст был в одном регистре.



Задача 2. Путь к файлу

Все данные сайта лежат в одном проекте. При написании кода, внутри этого проекта часто используются абсолютные пути файлов, которые необходимо проверять.



Пользователь вводит абсолютный путь к текстовому файлу, а также проверяемые данные: диск и расширение файла. Напишите программу, которая проверяет корректность этого пути.



Пример:

Путь к файлу: C:/user/docs/folder/new_file.txt

На каком диске должен лежать файл: C

Требуемое расширение файла: .txt

Путь корректен!



Задача 3. Удаление части

На вход в программу подаётся строка, состоящая из прописных и заглавных букв кириллицы. Напишите код, который проверяет, каких букв в строке больше, прописных или заглавных. Если заглавных букв больше, то сделать все буквы строки заглавными, иначе сделать все прописными.

Подсказка: используйте методы islower() и/или isupper().



Пример:

Введите строку: ПитоН - этО хорошО



Результат: питон - это хорошо



Пример 2:

Введите строку: ПиТоН - ЭтО УДоБнО



Результат: ПИТОН - ЭТО УДОБНО