import webbrowser

a=int(input("""     1. Normal linux commands\n     2. docker container\n"""))

if a == 1:
    webbrowser.open("C:/Users/Arya/Desktop/cgi.html")
elif a == 2:
    webbrowser.open("C:/Users/Arya/Desktop/docker.html")
else:
    print("Wrong Input")