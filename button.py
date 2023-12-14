import  pygame

class Button:
    def __init__(self, image, position, size, action):
        self.action = action
        self.image = image
        self.rect = self.image.get_rect(topleft=position)
        self.image = pygame.transform.scale(self.image, size)  # Установка размера изображения
        self.clicked = False  # Добавляем флаг для отслеживания нажатия

    def is_clicked(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos) and not self.clicked:  # Проверяем флаг нажатия
            self.action()
            self.clicked = True  # Устанавливаем флаг в True
            print("Кнопка нажата")

    def reset(self):
        self.clicked = False  # Сбрасываем флаг при отпускании кнопки
