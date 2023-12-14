import pygame
from menu_window import MenuWindow
from singleplayer_window import SinglePlayerWindow
from multiplayer_window import MultiplayerWindow
from settings_window import SettingsWindow

# Инициализация Pygame
pygame.init()
# Создание экземпляров оконф
singleplayer_window = SinglePlayerWindow()
multiplayer_window = MultiplayerWindow()
settings_window = SettingsWindow()
menu_window = MenuWindow(settings_window)
current_window = menu_window  # Начальное окно (главное меню)

running = True
# В основном цикле обработки событий Pygame
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Обработка событий мыши вне блока обработки pygame.QUIT
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Проверяем, что нажата левая кнопка мыши
                x, y = event.pos
                if current_window == menu_window:  # Проверяем, что текущее окно - главное меню
                    if menu_window.settings_button.rect.collidepoint(x, y):
                        menu_window.settings_button.is_clicked((x, y))  # Вызываем метод is_clicked для кнопки

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
    elif keys[pygame.K_4]:  # Переход в окно настроек (пример: нажатие клавиши "4")
        current_window = menu_window


pygame.quit()