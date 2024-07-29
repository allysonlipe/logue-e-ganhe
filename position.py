import pyautogui
import time

print("Pressione Ctrl+C para parar o programa.")

try:
    while True:
        x, y = pyautogui.position()
        print(f"Posição do mouse: X={x} Y={y}")
        time.sleep(1)
except KeyboardInterrupt:
    print("Programa encerrado.")
