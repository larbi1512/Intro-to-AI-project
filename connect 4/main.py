from board import *
from game import *
from constaints import *
import pygame
pygame.font.init()

agent = {
    "human": 0,
    "AI": 1
}
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect 4")


def main():
    game = Game(agent["human"], agent["AI"], 6)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # this code will be replaced with bestMove and humanMove function
                game.make_move_human()
                WIN.fill((0, 0, 0))
                game.board.draw_board(WIN)
                pygame.display.update()
                game.make_move_AI()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                game.restart()

        WIN.fill((0, 0, 0))
        game.board.draw_board(WIN)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
