import time

tempo = time.time()
time.sleep(5)

print(f'Tempo total: {int((time.time() - tempo) // 600)} minuto(s) e {((time.time() - tempo) % 600):.0f} segundo(s)')