# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: InventoryMate
def delete_item(item_id, confirm=False):
    if item_id in inventory:
        if confirm or input(f"Удалить {inventory[item_id]['name']}? (y/n) ") == 'y':
            del inventory[item_id]
            print("Элемент удален.")
            return True
    print("Не удалось удалить элемент или подтверждение не получено.")
    return False

def delete_room(room_name, confirm=False):
    if room_name in rooms:
        items_to_delete = [k for k, v in inventory.items() if v['room'] == room_name]
        if items_to_delete and not (confirm or input(f"Удалить комнату '{room_name}' и {len(items_to_delete)} элементов? (y/n) ") == 'y'):
            print("Операция отменена.")
            return False
        for item_id in items_to_delete:
            del inventory[item_id]
        del rooms[room_name]
        print(f"Комната '{room_name}' и все её элементы удалены.")
        return True
    print(f"Комната '{room_name}' не найдена.")
    return False

def delete_tag(tag_name, confirm=False):
    items_to_delete = [k for k, v in inventory.items() if tag_name in v.get('tags', [])]
    if items_to_delete and not (confirm or input(f"Удалить тег '{tag_name}' и {len(items_to_delete)} элементов? (y/n) ") == 'y'):
        print("Операция отменена.")
        return False
    for item_id in items_to_delete:
        if tag_name in inventory[item_id].get('tags', []):
            inventory[item_id]['tags'].remove(tag_name)
    # Удаляем тег, если он больше не используется (опционально, здесь просто очищаем список)
    print(f"Тег '{tag_name}' удален из элементов.")
    return True
