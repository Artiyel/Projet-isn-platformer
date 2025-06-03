import pygame
import ctypes

pygame.init()
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), int(user32.GetSystemMetrics(1)*0.93)

window = pygame.display.set_mode(screensize)
fond = pygame.image.load("assets/fond_menu_1.png")
fond = pygame.transform.scale(fond, screensize)
window.blit(fond, (0, 0))
pygame.display.flip()
pygame.time.wait(2000)
pygame.quit()