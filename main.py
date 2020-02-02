import sys

import pygame

from load_image import load_image
from paddle import Paddle
from ball import Ball
from score_counter import ScoreCounter
from line import Line


FPS = 60
WIDTH, HEIGHT = 800, 600
COLORS = (pygame.Color('white'), pygame.Color('yellow'), pygame.Color('black'))
screen, clock = None, None


def terminate():
    pygame.quit()
    sys.exit()


def start_menu():
    background = pygame.transform.scale(load_image('background.jpg'), (WIDTH, HEIGHT))
    screen.blit(background, (0, 0))
    font = pygame.font.Font(None, 80)

    start_button = font.render('Начать игру', 1, COLORS[0], COLORS[2])
    start_button_rect = start_button.get_rect()
    start_button_rect.center = (WIDTH // 2, HEIGHT // 2 - 60)
    screen.blit(start_button, start_button_rect)

    quit_button = font.render('Выйти на рабочий стол', 1, COLORS[0], COLORS[2])
    quit_button_rect = quit_button.get_rect()
    quit_button_rect.center = (WIDTH // 2, HEIGHT // 2 + 60)
    screen.blit(quit_button, quit_button_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit_screen()

            elif event.type == pygame.MOUSEMOTION:
                if start_button_rect.collidepoint(event.pos):
                    start_button = font.render('Начать игру', 1, COLORS[1], COLORS[2])
                else:
                    start_button = font.render('Начать игру', 1, COLORS[0], COLORS[2])

                if quit_button_rect.collidepoint(event.pos):
                    quit_button = font.render('Выйти на рабочий стол', 1, COLORS[1], COLORS[2])
                else:
                    quit_button = font.render('Выйти на рабочий стол', 1, COLORS[0], COLORS[2])

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    return
                elif quit_button_rect.collidepoint(event.pos):
                    exit_screen()

        screen.blit(background, (0, 0))
        screen.blit(start_button, start_button_rect)
        screen.blit(quit_button, quit_button_rect)

        pygame.display.flip()
        clock.tick(FPS)


def exit_screen():
    background = pygame.transform.scale(load_image('background.jpg'), (WIDTH, HEIGHT))
    screen.blit(background, (0, 0))
    font = pygame.font.Font(None, 60)

    exit_question = font.render('Вы уверены, что хотите выйти?', 1, COLORS[0], COLORS[2])
    exit_question_rect = exit_question.get_rect()
    exit_question_rect.center = (WIDTH // 2, HEIGHT // 2 - 30)
    screen.blit(exit_question, exit_question_rect)

    yes_button = font.render('Да', 1, COLORS[0], COLORS[2])
    yes_button_rect = yes_button.get_rect()
    yes_button_rect.center = (WIDTH // 2 - 50, HEIGHT // 2 + 30)
    screen.blit(yes_button, yes_button_rect)

    no_button = font.render('Нет', 1, COLORS[0], COLORS[2])
    no_button_rect = no_button.get_rect()
    no_button_rect.center = (WIDTH // 2 + 50, HEIGHT // 2 + 30)
    screen.blit(no_button, no_button_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            elif event.type == pygame.MOUSEMOTION:
                if yes_button_rect.collidepoint(event.pos):
                    yes_button = font.render('Да', 1, COLORS[1], COLORS[2])
                else:
                    yes_button = font.render('Да', 1, COLORS[0], COLORS[2])

                if no_button_rect.collidepoint(event.pos):
                    no_button = font.render('Нет', 1, COLORS[1], COLORS[2])
                else:
                    no_button = font.render('Нет', 1, COLORS[0], COLORS[2])

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if yes_button_rect.collidepoint(event.pos):
                    terminate()
                elif no_button_rect.collidepoint(event.pos):
                    return

        screen.blit(background, (0, 0))
        screen.blit(exit_question, exit_question_rect)
        screen.blit(yes_button, yes_button_rect)
        screen.blit(no_button, no_button_rect)

        pygame.display.flip()
        clock.tick(FPS)


def game():
    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill(COLORS[2])
    screen.blit(background, (0, 0))
    font = pygame.font.Font(None, 120)

    borders = pygame.sprite.Group()
    top_border = Line((0, 0), (WIDTH - 1, 0))
    bottom_border = Line((0, HEIGHT - 1), (WIDTH - 1, HEIGHT - 1))
    borders.add(top_border, bottom_border)

    gates = pygame.sprite.Group()
    left_gate = Line((0, 0), (0, HEIGHT - 1))
    right_gate = Line((WIDTH - 1, 0), (WIDTH - 1, HEIGHT - 1))
    gates.add(left_gate, right_gate)

    paddles = pygame.sprite.Group()
    left_paddle = Paddle((30, HEIGHT // 2), (30, 120), COLORS[0], HEIGHT)
    right_paddle = Paddle((WIDTH - 30, HEIGHT // 2), (30, 120), COLORS[0], HEIGHT)
    paddles.add(left_paddle, right_paddle)
    paddles.draw(screen)

    ball = Ball((WIDTH // 2, HEIGHT // 2), 7, 30, COLORS[0])
    screen.blit(ball.image, ball.rect)

    score_counters = pygame.sprite.Group()
    left_counter = ScoreCounter((200, HEIGHT // 2 - 200), 0, font, COLORS[0])
    right_counter = ScoreCounter((WIDTH - 200, HEIGHT // 2 - 200), 0, font, COLORS[0])
    score_counters.add(left_counter, right_counter)
    score_counters.draw(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit_screen()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if keys[pygame.K_s]:
                left_paddle.move(0)
            else:
                left_paddle.move(-12)
        elif keys[pygame.K_s]:
            left_paddle.move(12)
        else:
            left_paddle.move(0)

        if keys[pygame.K_UP]:
            if keys[pygame.K_DOWN]:
                right_paddle.move(0)
            else:
                right_paddle.move(-12)
        elif keys[pygame.K_DOWN]:
            right_paddle.move(12)
        else:
            right_paddle.move(0)

        res = ball.update(paddles, borders, gates)
        if res == 1:
            new_score = left_counter.get_score() + 1
            left_counter.change_score(new_score)
            if new_score >= 11:
                return -1
            left_paddle.set_default_pos()
            right_paddle.set_default_pos()
        elif res == -1:
            new_score = right_counter.get_score() + 1
            right_counter.change_score(new_score)
            if new_score >= 11:
                return 1
            left_paddle.set_default_pos()
            right_paddle.set_default_pos()

        screen.blit(background, (0, 0))
        paddles.draw(screen)
        screen.blit(ball.image, ball.rect)
        score_counters.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)


def game_over_screen(winner):
    background = pygame.transform.scale(load_image('background.jpg'), (WIDTH, HEIGHT))
    screen.blit(background, (0, 0))
    font = pygame.font.Font(None, 60)

    if winner == -1:
        game_over_text = font.render('Игра окончена! Игрок 1 победил!', 1, COLORS[0])
    else:
        game_over_text = font.render('Игра окончена! Игрок 2 победил!', 1, COLORS[0])
    game_over_text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200))
    screen.blit(game_over_text, game_over_text_rect)

    restart_question = font.render('Начать заново?', 1, COLORS[0])
    restart_question_rect = restart_question.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
    screen.blit(restart_question, restart_question_rect)

    yes_button = font.render('Да', 1, COLORS[0])
    yes_button_rect = yes_button.get_rect()
    yes_button_rect.center = (WIDTH // 2 - 50, HEIGHT // 2 + 30)
    screen.blit(yes_button, yes_button_rect)

    no_button = font.render('Нет', 1, COLORS[0])
    no_button_rect = no_button.get_rect()
    no_button_rect.center = (WIDTH // 2 + 50, HEIGHT // 2 + 30)
    screen.blit(no_button, no_button_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit_screen()

            elif event.type == pygame.MOUSEMOTION:
                if yes_button_rect.collidepoint(event.pos):
                    yes_button = font.render('Да', 1, COLORS[1])
                else:
                    yes_button = font.render('Да', 1, COLORS[0])

                if no_button_rect.collidepoint(event.pos):
                    no_button = font.render('Нет', 1, COLORS[1])
                else:
                    no_button = font.render('Нет', 1, COLORS[0])

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if yes_button_rect.collidepoint(event.pos):
                    return
                elif no_button_rect.collidepoint(event.pos):
                    terminate()

        screen.blit(background, (0, 0))
        screen.blit(game_over_text, game_over_text_rect)
        screen.blit(restart_question, restart_question_rect)
        screen.blit(yes_button, yes_button_rect)
        screen.blit(no_button, no_button_rect)

        pygame.display.flip()
        clock.tick(FPS)


def main():
    pygame.init()
    global screen, clock
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    start_menu()
    while True:
        result = game()
        game_over_screen(result)


if __name__ == '__main__':
    main()
