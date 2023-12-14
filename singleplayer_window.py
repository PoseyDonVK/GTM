import pygame

class SinglePlayerWindow:
    def __init__(self):
        self.window_width = 960
        self.window_height = 540
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        self.original_image = pygame.image.load('singlep.png')  # Путь к изображению для одиночной игры
        self.image = pygame.transform.scale(self.original_image, (self.window_width, self.window_height))

    def update(self):
        # Логика и обработка событий для одиночной игры

        self.window.fill((0, 0, 0))  # Очистка окна
        self.window.blit(self.image, (0, 0))  # Отображение изменённого изображения
        pygame.display.update()  # Обновление экрана
