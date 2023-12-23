import pygame

class MenuWindow:
    def __init__(self):
        self.window_width = 1200
        self.window_height = 800
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        self.original_image = pygame.image.load('project.jpg')  # Путь к изображению для главного меню
        self.image = pygame.transform.scale(self.original_image, (self.window_width, self.window_height))
        # Координаты и размеры кнопки "Settings"
        x = 0 # Здесь укажите координату x для кнопки настроек
        y = 0  # Здесь укажите координату y для кнопки настроек
        width = 200  # Здесь укажите ширину для кнопки настроек
        height = 50  # Здесь укажите высоту для кнопки настроек
        self.settings_button_rect = pygame.Rect(x, y, width, height)

    def update(self):
        # Логика и обработка событий для главного меню

        self.window.fill((0, 0, 0))  # Очистка окна
        self.window.blit(self.image, (0, 0))  # Отображение изменённого изображения
        pygame.display.update()  # Обновление экрана

