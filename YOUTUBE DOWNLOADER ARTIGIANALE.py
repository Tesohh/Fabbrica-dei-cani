import os
option = input("vuoi un file audio o video? ([a]udio/[v]ideo): ")
if option == "a":
    formato = input("Che formato audio vuoi?: ")
    url = input("Incolla qui l'url: ")
    os.system(f"youtube-dl -x --audio-format {formato} {url}")
    os.system("cls")
    print("Finito!")
    os.system("pause")
if option == "v":
    url = input("Incolla qui l'url: ")
    os.system(f"youtube-dl {url}")
    os.system("cls")
    print("Finito!")
    os.system("pause")
    


