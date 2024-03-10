import psutil

proc = "LeagueClient.exe"
run = True

print("oh such a beauty day with no league :D...")

while run:
    processes = psutil.process_iter()
    for process in processes:
        if proc in process.name():
            print("NO DONT PLAY LEAGUE NO")
            process.kill()
            
        
