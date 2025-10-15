def analyze_playlist(songs):
    total_seconds = sum(int(m)*60 + int(s) for m,s in [song["duration"].split(":") for song in songs])
    avg = total_seconds / len(songs)
    longest = max(songs, key=lambda s: int(s["duration"].split(":")[0])*60 + int(s["duration"].split(":")[1]))
    shortest = min(songs, key=lambda s: int(s["duration"].split(":")[0])*60 + int(s["duration"].split(":")[1]))
    fit_30 = 30*60 // avg
    print(f"Total Duration: {total_seconds//60}m {total_seconds%60}s")
    print(f"Average Song: {int(avg//60)}m {int(avg%60)}s")
    print(f"Longest: {longest['title']}, Shortest: {shortest['title']}")
    print(f"Songs that fit in 30 mins: {int(fit_30)}")


songs = [
    {"title": "Song A", "duration": "3:45"},
    {"title": "Song B", "duration": "4:20"},
    {"title": "Song C", "duration": "2:55"}
]
analyze_playlist(songs)