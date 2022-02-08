import pygame, requests, sys, os


class MapParams(object):
    def __init__(self):
        self.x = 65.665279
        self.y = 50.813492
        self.zoom = 5
        self.type = "map"

    def ll(self):
        return str(self.y) + "," + str(self.x)

    def update(self, event):
        if event.key == pygame.K_PAGEUP and self.zoom < 19:
            self.zoom += 1
        elif event.key == pygame.K_PAGEUP and self.zoom > 2:
            self.zoom -= 1


def load_map(mp):
    map_request = "http://static-maps.yandex.ru/1.x/?ll={ll}&z={z}&l={type}".format(ll=mp.ll(), z=mp.zoom, type=mp.type)
    response = requests.get(map_request)
    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    map_file = "map.png"
    try:
        with open(map_file, "wb") as file:
            file.write(response.content)
    except IOError as ex:
        print("Ошибка записи временного файла:", ex)
        sys.exit(2)
    return map_file



# Удаляем за собой файл с изображением.
os.remove(map_file)
