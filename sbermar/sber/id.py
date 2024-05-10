def decode_fields(encoded, translations):
    decoded = []
    
    for obj in encoded:
        new_obj = {}
        for key, value in obj.items():
            if key.endswith('id'):
                # Расшифровываем поле, если оно заканчивается на 'id'
                try:
                    new_value = translations[value]
                except KeyError:
                    # Если значение не найдено в словаре, оставляем его без изменений
                    new_value = value
            else:
                # Оставляем поле без изменений, если оно не заканчивается на 'id'
                new_value = value
            
            # Проверяем, нужно ли исключить это поле
            if key not in {'groupId', 'service', 'formatSize', 'ca'}:
                new_obj[key] = new_value
        
        # Добавляем объект в список после обработки всех полей
        decoded.append(new_obj)
    
    return decoded

# Пример использования функции
encoded = [{'groupId': 'group1', 'service': 'service1', 'formatSize': 'size1', 'ca': 'ca1', 'itemId': 'item1'},
           {'groupId': 'group2', 'service': 'service2', 'formatSize': 'size2', 'ca': 'ca2', 'itemId': 'item2'}]
translations = {'item1': 'Item A', 'item2': 'Item B'}
decoded = decode_fields(encoded, translations)
print(decoded)

unique_ids = set([obj['itemId'] for obj in encoded])
print(unique_ids)