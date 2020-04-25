from pygame.locals import *
import pygame
import sys
import subprocess
from subprocess import Popen
from time import  sleep
cmd = "C:\\Users\\shino\\Anaconda3\\envs\\game\\python.exe C:\\rep\\cool104\\game_main.py"


def main():
    pygame.init()  # Pygameを初期化
    screen = pygame.display.set_mode((200, 100))  # 画面を作成
    pygame.display.set_caption("cool104")  # タイトルを作成

    button = pygame.Rect(30, 30, 120, 50)  # creates a rect object
    #button2 = pygame.Rect(100, 30, 70, 50)  # creates a rect object

    # STEP1.フォントの用意
    font = pygame.font.SysFont(None, 25)

    # STEP2.テキストの設定
    text1 = font.render("Push me!", True, (0, 0, 0))
    #text2 = font.render("GREEN", True, (0, 0, 0))

    running = True

    proc = ""
    # メインループ
    while running:
        screen.fill((0, 0, 0))  # 画面を黒で塗りつぶす

        pygame.draw.rect(screen, (255, 0, 0), button)
        #pygame.draw.rect(screen, (0, 255, 0), button2)

        screen.blit(text1, (40, 45))
        #screen.blit(text2, (105, 45))

        pygame.display.update()  # 描画処理を実行
        for event in pygame.event.get():
            if event.type == QUIT:  # 終了イベント
                running = False
                pygame.quit()  # pygameのウィンドウを閉じる
                sys.exit()  # システム終了

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    if proc == "":
                        proc = Popen(cmd)
                    else:
                        proc.terminate()
                        proc = Popen(cmd)
                #if button2.collidepoint(event.pos):
                    #proc.terminate()
if __name__ == "__main__":
    main()


