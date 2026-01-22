import pytest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
#----------------------------------------add_new_book------------------------------------
    #метод add_new_book. Положительные проверки на количество символов в названии
    #1,2,32,39,40 символов
    @pytest.mark.parametrize('name', ['Г', 
                                      'Го', 
                                      'Гордость и предубеждение и зомби',
                                      'Гордость и предубеждение и зомби. Том 1',
                                      'Гордость и предубеждение и зомби. Том 1.'])
    def test_add_new_book_positive_addition_allowed_number_characters(self,name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.books_genre

    #Метод add_new_book. Негативные проверки на количество символов
    #0,41
    @pytest.mark.parametrize('name', ['', 
                                      'Гордость и предубеждение и зомби. Том 11.'])
    def test_add_new_book_negative_addition_disallowed_number_characters(self,name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.books_genre

    #Метод add_new_book. Негативная проверка добавления существующего названия
    def test_add_new_book_negative_addition_exists_name_not_increase_count(self):
        collector = BooksCollector()
        name="Гордость"
        collector.add_new_book(name)
        size = len(collector.books_genre)
        collector.add_new_book(name)
        assert len(collector.books_genre) == size

    #Метод add_new_book. Проверка что при добавлении книги жанр не устанавливается
    def test_add_new_book_genre_is_none(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость')
        assert collector.books_genre.get('Гордость') is None

#----------------------------------------set_book_genre------------------------------------
    def test_set_book_genre_valid(self):
        name = 'Книга'
        genre = 'Фантастика'
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_set_book_genre_invalid_genre(self):
        name = 'Книга'
        genre = 'Недопустимый жанр'
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        # Жанр не должен измениться, так как он недопустим
        assert collector.get_book_genre(name) != genre

    def test_set_book_genre_nonexistent_book(self):
        collector = BooksCollector()
        name = 'Несуществующая книга'
        genre = 'Фантастика'
        collector.set_book_genre(name, genre)
        assert name not in collector.books_genre

#----------------------------------------get_book_genre------------------------------------        
    #Позитивные проверки метода get_book_genre
    #Книга есть, жанр установлен
    def test_get_book_genre_existing_book_with_genre(self):
        collector = BooksCollector()
        name = 'Гарри Поттер'
        genre = 'Фантастика'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        test_genre = collector.get_book_genre(name)
        assert test_genre == genre

    #Книга есть, жанр не установлен
    def test_get_book_genre_existing_book_without_genre(self):
        collector = BooksCollector()
        name = 'Гарри Поттер'
        collector.add_new_book(name)  # жанр не установлен

        test_genre = collector.get_book_genre(name)
        assert test_genre is None

    #Негативные проверки метода get_book_genre
    #Книги нет в коллекции
    def test_get_book_genre_nonexistent_book(self):
        collector = BooksCollector()
        name = 'Гарри Поттер'
        test_genre = collector.get_book_genre(name)
        assert test_genre is None

    #Пустое имя книги
    def test_get_book_genre_empty_string_name(self):
        collector = BooksCollector()
        test_genre = collector.get_book_genre('')
        assert test_genre is None

#----------------------------------------get_books_with_specific_genre------------------------------------                
    #Позитивные проверки метода get_books_with_specific_genre

    #Одна книга с нужным жанром
    def test_get_books_with_specific_genre_one_book(self):
        collector = BooksCollector()
        name='Гарри Поттер'
        genre='Фантастика'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        books = collector.get_books_with_specific_genre(genre)
        assert books == [name]

    #Несколько книг с одним жанром
    def test_get_books_with_specific_genre_multiple_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('Властелин колец', 'Фантастика')

        books = collector.get_books_with_specific_genre('Фантастика')
        assert set(books) == {'Гарри Поттер', 'Властелин колец'}
    
    #Часть книг с нужным жанром
    def test_get_books_with_specific_genre_partial_match(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('Властелин колец', 'Детективы')

        books = collector.get_books_with_specific_genre('Фантастика')
        assert books == ['Гарри Поттер']

    #Негативные проверки метода get_books_with_specific_genre

    #Нет книг с нужным жанром
    def test_get_books_with_specific_genre_no_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')

        books = collector.get_books_with_specific_genre('Детективы')
        assert books == []

    #Книги без жанра
    def test_get_books_with_specific_genre_books_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')  # жанр не установлен

        books = collector.get_books_with_specific_genre('Фантастика')
        assert books == []

    #Пустой словарь книг
    def test_get_books_with_specific_genre_empty_collector(self):
        collector = BooksCollector()
        books = collector.get_books_with_specific_genre('Фантастика')
        assert books == []

    #Неверный (несуществующий) жанр (не входит в self.genre)
    def test_get_books_with_specific_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')

        books = collector.get_books_with_specific_genre('Романтика')
        assert books == []

#----------------------------------------books_genre------------------------------------
    #Пустой словарь при новом экземпляре
    def test_get_books_genre_empty_on_init(self):
        collector = BooksCollector()
        books = collector.get_books_genre()
        assert books == {}

    #После добавления одной книги
    def test_get_books_genre_one_book_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        books = collector.get_books_genre()
        assert 'Гарри Поттер' in books
        # жанр по умолчанию пустой
        assert books['Гарри Поттер'] == None

    #После добавления нескольких книг
    def test_get_books_genre_multiple_books_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Властелин колец')
        books = collector.get_books_genre()
        assert set(books.keys()) == {'Гарри Поттер', 'Властелин колец'}

    #Книга с установленным жанром
    def test_get_books_genre_book_with_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        books = collector.get_books_genre()
        assert books['Гарри Поттер'] == 'Фантастика'

#----------------------------------------get_books_for_children------------------------------------
    #Позитивные проверки метода get_books_for_children
    #  Одна детская книга
    def test_get_books_for_children_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Мадагаскар')
        collector.set_book_genre('Мадагаскар', 'Мультфильмы')

        books = collector.get_books_for_children()
        assert books == ['Мадагаскар']

    #Несколько детских книг
    def test_get_books_for_children_multiple_books(self):
        collector = BooksCollector()
        collector.add_new_book('Мадагаскар')
        collector.add_new_book('Шрек')
        collector.set_book_genre('Мадагаскар', 'Мультфильмы')
        collector.set_book_genre('Шрек', 'Комедии')

        books = collector.get_books_for_children()
        assert set(books) == {'Мадагаскар', 'Шрек'}

    #Смешанные жанры
    def test_get_books_for_children_mixed_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Мадагаскар')
        collector.add_new_book('Дракула')
        collector.add_new_book('Шрек')

        collector.set_book_genre('Мадагаскар', 'Мультфильмы')  # детский
        collector.set_book_genre('Дракула', 'Ужасы')           # возрастной
        collector.set_book_genre('Шрек', 'Комедии')            # детский

        books = collector.get_books_for_children()
        assert set(books) == {'Мадагаскар', 'Шрек'}
    
    #Негативные проверки метода get_books_for_children

    #Книги с возрастным рейтингом (не подходят детям)
    def test_get_books_for_children_books_with_age_rating_excluded(self):
        collector = BooksCollector()
        collector.add_new_book('Дракула')
        collector.set_book_genre('Дракула', 'Ужасы')  # есть возрастной рейтинг

        books = collector.get_books_for_children()
        assert books == []

    #Книги без жанра
    def test_get_books_for_children_books_without_genre_excluded(self):
        collector = BooksCollector()
        collector.add_new_book('Мадагаскар')  # жанр не установлен

        books = collector.get_books_for_children()
        assert books == []

    #Книги с жанром вне списка self.genre
    def test_get_books_for_children_invalid_genre_excluded(self):
        collector = BooksCollector()
        collector.add_new_book('Книга X')
        collector.set_book_genre('Книга X', 'Романтика')  # жанр не в self.genre

        books = collector.get_books_for_children()
        assert books == []

    #Пустая коллекция
    def test_get_books_for_children_empty_collector(self):
        collector = BooksCollector()
        books = collector.get_books_for_children()
        assert books == []

#----------------------------------------add_book_in_favorites------------------------------------
    # Добавление книги в избранное
    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')

        assert 'Гарри Поттер' in collector.get_list_of_favorites_books()
        assert len(collector.get_list_of_favorites_books()) == 1

    # Попытка добавить книгу, которой нет в books_genre
    def test_add_book_in_favorites_nonexistent_book(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Властелин колец')  # книга не добавлена

        assert collector.get_list_of_favorites_books() == []

    # Попытка добавить одну и ту же книгу дважды
    def test_add_book_in_favorites_no_duplicates(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')  # повторное добавление

        favorites = collector.get_list_of_favorites_books()
        assert favorites.count('Гарри Поттер') == 1
        assert len(favorites) == 1

    # Добавление нескольких книг в избранное
    def test_add_book_in_favorites_multiple_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Шерлок Холмс')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Шерлок Холмс')

        favorites = collector.get_list_of_favorites_books()
        assert set(favorites) == {'Гарри Поттер', 'Шерлок Холмс'}
        assert len(favorites) == 2

    # Проверка, что после удаления книги из favorites, можно добавить её снова
    def test_add_book_in_favorites_after_removal(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.delete_book_from_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')

        favorites = collector.get_list_of_favorites_books()
        assert favorites == ['Гарри Поттер']

#----------------------------------------delete_book_from_favorites------------------------------------
     # Успешное удаление книги из избранного
    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')

        collector.delete_book_from_favorites('Гарри Поттер')
        assert collector.get_list_of_favorites_books() == []

    # Попытка удалить книгу, которой нет в избранном (ничего не меняется)
    def test_delete_book_from_favorites_not_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        # книга не добавлялась в избранное
        collector.delete_book_from_favorites('Гарри Поттер')

        assert collector.get_list_of_favorites_books() == []

    # Попытка удалить несуществующую книгу (в books_genre нет)
    def test_delete_book_from_favorites_nonexistent_book(self):
        collector = BooksCollector()
        collector.delete_book_from_favorites('Властелин колец')  # книги нет в коллекции

        assert collector.get_list_of_favorites_books() == []

    # Удаление одной книги из нескольких в избранном
    def test_delete_book_from_favorites_one_of_multiple(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Шерлок Холмс')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Шерлок Холмс')

        collector.delete_book_from_favorites('Гарри Поттер')
        favorites = collector.get_list_of_favorites_books()
        assert favorites == ['Шерлок Холмс']

    # Удаление всех книг из избранного
    def test_delete_book_from_favorites_all(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Шерлок Холмс')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Шерлок Холмс')

        collector.delete_book_from_favorites('Гарри Поттер')
        collector.delete_book_from_favorites('Шерлок Холмс')
        favorites = collector.get_list_of_favorites_books()
        assert favorites == []

#----------------------------------------get_list_of_favorites_books------------------------------------        
     # Проверка, что список избранного пуст при создании экземпляра
    def test_get_list_of_favorites_books_empty_on_init(self):
        collector = BooksCollector()
        favorites = collector.get_list_of_favorites_books()
        assert favorites == []

    # Проверка, что добавленные книги появляются в избранном
    def test_get_list_of_favorites_books_after_adding(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Шерлок Холмс')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Шерлок Холмс')

        favorites = collector.get_list_of_favorites_books()
        assert set(favorites) == {'Гарри Поттер', 'Шерлок Холмс'}
        assert len(favorites) == 2

    # Проверка, что повторное добавление книги не дублирует её
    def test_get_list_of_favorites_books_no_duplicates(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')  # повторное добавление

        favorites = collector.get_list_of_favorites_books()
        assert favorites == ['Гарри Поттер']
        assert len(favorites) == 1

    # Проверка, что удаление книги обновляет список избранного
    def test_get_list_of_favorites_books_after_deletion(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Шерлок Холмс')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Шерлок Холмс')

        collector.delete_book_from_favorites('Гарри Поттер')
        favorites = collector.get_list_of_favorites_books()
        assert favorites == ['Шерлок Холмс']

    # Проверка, что после удаления всех книг список пуст
    def test_get_list_of_favorites_books_after_deleting_all(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')

        collector.delete_book_from_favorites('Гарри Поттер')
        favorites = collector.get_list_of_favorites_books()
        assert favorites == []