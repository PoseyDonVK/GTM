import pygame
from  button import Button

class MenuWindow:

    def __init__(self, settings_window):
        self.window_width = 960
        self.window_height = 540
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        self.original_image = pygame.image.load('menu.jpg')  # Путь к изображению для главного меню
        # Передача экземпляра окна настроек в MenuWindow
        self.settings_window = settings_window
        new_width = 50  # Новая ширина кнопки
        new_height = 50  # Новая высота кнопки
        self.image = pygame.transform.scale(self.original_image, (self.window_width, self.window_height))
        x = 30
        y = 450
        # Загрузка изображения для кнопки перехода в настройки
        settings_button_image = pygame.image.load('project_settings_button_.png')
        # Создание кнопки и указание действия при нажатии
        self.settings_button = Button(settings_button_image, (x, y), (new_width, new_height), self.go_to_settings)

    def update(self):
        # Логика и обработка событий для главного меню
        self.window.fill((0, 0, 0))  # Очистка окна
        self.window.blit(self.image, (0, 0))  # Отображение изменённого изображения
        # Отображение кнопки на экране
        self.window.blit(self.settings_button.image, self.settings_button.rect.topleft)
        pygame.display.update()  # Обновление экрана

        # Проверка нажатия кнопки настройки
        mouse_pos = pygame.mouse.get_pos()
        if self.settings_button.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:  # Проверяем, что левая кнопка мыши нажата
                self.settings_button.is_clicked(mouse_pos)

    def go_to_settings(self):
        global current_window  # Обращение к глобальной переменной current_window
        if self.settings_window:
            current_window = self.settings_window  # Изменение текущего окна на окно настроек
        else:
            print("Ошибка: Окно настроек не инициализировано")


