import pygame
from menu_window import MenuWindow
from singleplayer_window import SinglePlayerWindow
from multiplayer_window import MultiplayerWindow
from settings_window import SettingsWindow

# Инициализация Pygame
pygame.init()

# Создание экземпляров окон
menu_window = MenuWindow()
singleplayer_window = SinglePlayerWindow()
multiplayer_window = MultiplayerWindow()
settings_window = SettingsWindow()

current_window = menu_window  # Начальное окно (главное меню)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Выход из цикла при закрытии окна

        # Обработка события изменения размера окна
        if event.type == pygame.VIDEORESIZE:
            new_width, new_height = event.size
            window = pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)

    # Обновление текущего окна
    current_window.update()

    # Логика перехода между окнами (можно настроить условия для перехода)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:  # Переход в окно одиночной игры (пример: нажатие клавиши "1")
        current_window = singleplayer_window
    elif keys[pygame.K_2]:  # Переход в окно сетевой игры (пример: нажатие клавиши "2")
        current_window = multiplayer_window
    elif keys[pygame.K_3]:  # Переход в окно настроек (пример: нажатие клавиши "3")
        current_window = settings_window
    elif keys[pygame.K_4]:  # Переход в окно настроек (пример: нажатие клавиши "3")
        current_window = menu_window


pygame.quit()
