from pytube import YouTube
link = input('Enter the You Tube link 》  ')
ytb = YouTube(link)
videos = ytb.streams.all()
i = 1
for stream in videos:
	print(str(i) + "  _  " + str(stream))
	i += 1
stream_number = int(input("Enter Number 》   "))
video = videos[stream_number - 1]
video.download()
