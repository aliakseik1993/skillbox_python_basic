films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
favorite_films = []
def exist_film(current_film, films_list):
    for film in films_list:
        if film == current_film:
            return True
    return False
while True:
    print("Ваш текущий топ фильмов")
    print(favorite_films)
    new_movie = input("Введите название фильма: ")
    if exist_film(new_movie, films) == True:
        print("Команды: добавить, вставить, удалить")
        answer = input("Введите команду: ")
        if exist_film(new_movie, favorite_films) == True and answer != "удалить":
            print("такой фильм уже есть в вашем котологе топ фильмов")
        else:
            if answer == "добавить":
                favorite_films.append(new_movie)
            if answer == "удалить":
                if exist_film(new_movie, favorite_films):
                    favorite_films.remove(new_movie)
                else:
                    print("Такого фильма нет в вашем списке")
            if answer == "Вставить":
                possition = int(input("На какое место поставить? "))
                if possition <= len(favorite_films):
                    favorite_films.insert(possition - 1, new_movie)
                else:
                    print("Вы выбрали неправильную позицию")
    else:
        print("Такого фильма нет в котологе сайта")