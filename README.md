#----------------------------------------add_new_book------------------------------------
    #метод add_new_book. Положительные проверки на количество символов в названии
    #1,2,32,39,40 символов
    test_add_new_book_positive_addition_allowed_number_characters

    #Метод add_new_book. Негативные проверки на количество символов
    #0,41
    test_add_new_book_negative_addition_disallowed_number_characters
        
    #Метод add_new_book. Негативная проверка добавления существующего названия
    test_add_new_book_negative_addition_exists_name_not_increase_count
        
    #Метод add_new_book. Проверка что при добавлении книги жанр не устанавливается
    test_add_new_book_genre_is_none

#----------------------------------------set_book_genre------------------------------------
    #успешная установка жанра 
    test_set_book_genre_valid

    #неуспешная установка несуществующего жанра 
    test_set_book_genre_invalid_genre

    #неуспешная установка жанра для несуществующей книги
    test_set_book_genre_nonexistent_book
    
#----------------------------------------get_book_genre------------------------------------        
    #Позитивные проверки метода get_book_genre
    #Книга есть, жанр установлен
    test_get_book_genre_existing_book_with_genre

    #Книга есть, жанр не установлен
    test_get_book_genre_existing_book_without_genre

    #Негативные проверки метода get_book_genre
    #Книги нет в коллекции
    test_get_book_genre_nonexistent_book
    
    #Пустое имя книги
    test_get_book_genre_empty_string_name

#----------------------------------------get_books_with_specific_genre------------------------------------                
    #Позитивные проверки метода get_books_with_specific_genre

    #Одна книга с нужным жанром
    test_get_books_with_specific_genre_one_book

    #Несколько книг с одним жанром
    test_get_books_with_specific_genre_multiple_books
    
    #Часть книг с нужным жанром
    test_get_books_with_specific_genre_partial_match

    #Негативные проверки метода get_books_with_specific_genre

    #Нет книг с нужным жанром
    test_get_books_with_specific_genre_no_books

    #Книги без жанра
    test_get_books_with_specific_genre_books_without_genre

    #Пустой словарь книг
    test_get_books_with_specific_genre_empty_collector

    #Неверный (несуществующий) жанр (не входит в self.genre)
    test_get_books_with_specific_genre_invalid_genre

#----------------------------------------books_genre------------------------------------
    #Пустой словарь при новом экземпляре
    test_get_books_genre_empty_on_init

    #После добавления одной книги
    test_get_books_genre_one_book_added

    #После добавления нескольких книг
    test_get_books_genre_multiple_books_added

    #Книга с установленным жанром
    test_get_books_genre_book_with_genre

#----------------------------------------get_books_for_children------------------------------------
    #Позитивные проверки метода get_books_for_children
    #  Одна детская книга
    test_get_books_for_children_one_book

    #Несколько детских книг
    test_get_books_for_children_multiple_books

    #Смешанные жанры
    test_get_books_for_children_mixed_genres
            
    #Негативные проверки метода get_books_for_children

    #Книги с возрастным рейтингом (не подходят детям)
    test_get_books_for_children_books_with_age_rating_excluded
        
    #Книги без жанра
    test_get_books_for_children_books_without_genre_excluded
    
    #Книги с жанром вне списка self.genre
    test_get_books_for_children_invalid_genre_excluded

    #Пустая коллекция
    test_get_books_for_children_empty_collector

#----------------------------------------add_book_in_favorites------------------------------------
    # Добавление книги в избранное
    test_add_book_in_favorites_success

    # Попытка добавить книгу, которой нет в books_genre
    test_add_book_in_favorites_nonexistent_book

    # Попытка добавить одну и ту же книгу дважды
    test_add_book_in_favorites_no_duplicates

    # Добавление нескольких книг в избранное
    test_add_book_in_favorites_multiple_books

    # Проверка, что после удаления книги из favorites, можно добавить её снова
    test_add_book_in_favorites_after_removal

#----------------------------------------delete_book_from_favorites------------------------------------
    # Успешное удаление книги из избранного
    test_delete_book_from_favorites_success
        
    # Попытка удалить книгу, которой нет в избранном (ничего не меняется)
    test_delete_book_from_favorites_not_in_favorites

    # Попытка удалить несуществующую книгу (в books_genre нет)
    test_delete_book_from_favorites_nonexistent_book

    # Удаление одной книги из нескольких в избранном
    test_delete_book_from_favorites_one_of_multiple
        

    # Удаление всех книг из избранного
    test_delete_book_from_favorites_all

#----------------------------------------get_list_of_favorites_books------------------------------------        
    # Проверка, что список избранного пуст при создании экземпляра
    test_get_list_of_favorites_books_empty_on_init

    # Проверка, что добавленные книги появляются в избранном
    test_get_list_of_favorites_books_after_adding

    # Проверка, что повторное добавление книги не дублирует её
    test_get_list_of_favorites_books_no_duplicates

    # Проверка, что удаление книги обновляет список избранного
    test_get_list_of_favorites_books_after_deletion

    # Проверка, что после удаления всех книг список пуст
    test_get_list_of_favorites_books_after_deleting_all 