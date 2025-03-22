import pygame
import random
import time
import textwrap

pygame.init()

# Window settings
width, height = 900, 650
background_colour = (30, 30, 30)
bar_colour = (100, 200, 255)
highlight_colour = (255, 100, 100)
text_colour = (255, 255, 255)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sorting Algorithm Visualizer")

# Sorting settings
ARRAY_SIZE = 50
SORT_SPEED = 0.015 
data = []

def generate_data(size):
    return [random.randint(10, height - 100) for _ in range(size)]

data = generate_data(ARRAY_SIZE)
bar_width = width // ARRAY_SIZE

def draw_bars(data, highlight=None):
    screen.fill(background_colour)
    for i, val in enumerate(data): 
        color = highlight_colour if highlight and i in highlight else bar_colour
        pygame.draw.rect(screen, color, (i * bar_width, height - val - 50, bar_width - 2, val))
    font = pygame.font.Font(None, 28)
    instructions = ["Press: B for Bubble Sort", "Press: M for Merge Sort", "Press: Q for Quick Sort"]

    max_line_width = 200  
    wrapped_instructions = []
    for text in instructions:
        wrapped_lines = textwrap.wrap(text, width=max_line_width)
        wrapped_instructions.extend(wrapped_lines)
        
    background_color = (50, 50, 50)
    padding = 10  
    for i, text in enumerate(wrapped_instructions):
        rendered_text = font.render(text, True, text_colour)
        text_rect = rendered_text.get_rect()
        text_rect.topleft = (10, 10 + i * 30) 
        pygame.draw.rect(screen, background_color, (text_rect.x - padding, text_rect.y - padding,
                                                     text_rect.width + 2 * padding, text_rect.height + 2 * padding))
        screen.blit(rendered_text, text_rect.topleft)
    pygame.display.update()


# Bubble Sort
def bubble_sort(data):
    n = len(data)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            draw_bars(data, highlight=[j, j + 1])
            time.sleep(SORT_SPEED)
            if data[j] > data[j + 1]:  
                data[j], data[j + 1] = data[j + 1], data[j]
    draw_bars(data)

# Merge Sort
def merge_sort(data, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(data, left, mid)
        merge_sort(data, mid + 1, right)
        merge(data, left, mid, right)

def merge(data, left, mid, right):
    left_part = data[left:mid + 1]
    right_part = data[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        draw_bars(data, highlight=[k])
        time.sleep(SORT_SPEED)
        if left_part[i] < right_part[j]:
            data[k] = left_part[i]
            i += 1
        else:
            data[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        draw_bars(data, highlight=[k])
        time.sleep(SORT_SPEED)
        data[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        draw_bars(data, highlight=[k])
        time.sleep(SORT_SPEED)
        data[k] = right_part[j]
        j += 1
        k += 1

def quick_sort(data, low, high):
    if low < high:
        pivot_index = partition(data, low, high)
        quick_sort(data, low, pivot_index - 1)
        quick_sort(data, pivot_index + 1, high)

def partition(data, low, high):
    pivot = data[high]
    i = low - 1

    for j in range(low, high):
        draw_bars(data, highlight=[j, high]) 
        time.sleep(SORT_SPEED)
        if data[j] < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]

    data[i + 1], data[high] = data[high], data[i + 1]
    draw_bars(data, highlight=[i + 1]) 
    time.sleep(SORT_SPEED)
    return i + 1


def main():
    running = True
    sorting = False

    while running:
        screen.fill(background_colour)
        draw_bars(data)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b and not sorting:
                    sorting = True
                    bubble_sort(data)
                    sorting = False
                elif event.key == pygame.K_m and not sorting:
                    sorting = True
                    merge_sort(data, 0, len(data) - 1)
                    draw_bars(data)
                    sorting = False
                elif event.key == pygame.K_q and not sorting:
                    sorting = True
                    quick_sort(data, 0, len(data) - 1)
                    draw_bars(data) 
                    sorting = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
