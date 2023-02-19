# Тест №1
def test_add_new_pet_with_valid_data_without_photo(name='Рекс', animal_type='Собака',
                                                   age='7'):
    """Проверяем что можно добавить питомца с корректными данными, но без фото"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


# Тест №2
def test_add_photo_of_pet(pet_photo='images/s1200.jpg'):
    """Проверяем возможность добавления фото в созданного питомца без фото"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берем первого питомца и добавляем его фото
    status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)

    # Проверяем , что статус ответа = 200 и у питомца появилось фото
    assert status == 200
    assert result['pet_photo'] != ''


# Тест №3
def test_add_new_pet_with_invalid_pet_photo(name='Микки', animal_type='Собака',
                                            age='100',
                                            pet_photo=' '):
    """Проверяем, что нельзя добавить питомца, если не указан путь до файла с фото"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца

    try:
        status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    except PermissionError:

        print("Specify the path to the file")


# Тест №4
def test_get_api_key_for_invalid_user(email=valid_email, password='11111'):
    """ Проверяем, что при вводе неверного пароля, запрос api ключа не удается, и возвращается статус 403"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403


# Тест №5
def test_add_new_pet_with_negative_age(name='Микки', animal_type='Собака',
                                       age='-4', pet_photo='images/155.jpg'):
    """Проверяем, что нельзя добавить питомца с отрицательным возрастом"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 500


# Тест №6
def test_add_new_pet_without_data_with_photo(name='', animal_type='',
                                             age='', pet_photo='images/155.jpg'):
    """Проверяем, что нельзя добавить питомца без данных, но с фото"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 500


# Тест №7
def test_add_new_pet_with_unacceptable_name(name=',;:%№)', animal_type='Собака',
                                            age='100', pet_photo='images/155.jpg'):
    """Проверяем, что нельзя добавить питомца с именем из символов"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 500


# Тест №8
def test_add_new_pet_with_unacceptable_animal_type(name='Рекс', animal_type='.,:%№№%::',
                                                   age='100', pet_photo='images/155.jpg'):
    """Проверяем, что нельзя добавить питомца с породой из символов"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 500


# Тест №9
def test_add_new_pet_with_no_data(name='', animal_type='',
                                  age=''):
    """Проверяем возможность добавления нового питомца без данных"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца без фото
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == ''
    assert result['pet_photo'] == ''


# Тест №10
def test_get_api_key_for_invalid_user(email='$%jhg@mail.ru', password=valid_password):
    """ Проверяем, что при вводе неверного email, запрос api ключа не удается, и возвращается статус 403"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
