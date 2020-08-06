# VideoCombiner

### What It Does
Stitches together "split" video files into one singular file.

### Why
The impetus for this was that in a particular class, the professor split up the recorded lectures into "atomic units," e.g., a lecture would be split into five video lectures, suffixed by `P1`, `P2`, `P3`, etc.

I actually enjoyed this, since it made watching the lectures psychologically easier, but a particular student on the message board was kvetching about why this was done, for which I'm sure several people held their tongue of "throw it into a playlist, dude."

Being ornery at the moment, I decided to "help" the troubled student by writing this quick script, which stitches together the parted out lectures into singular lectures. It only depends on `ffmpeg` being on your system. I believe I could have done this in a singular convoluted Bash invocation, but to clean it up a little, I made it a python script. 

### Conclusion
In the student's defense, we later found out there were some other stuff going on, and he was just lashing out at the most recent, perceived inconvenience. But, the script was already written, and as such, it's being checked in. 

And, there **was** an interesting technological piece. I originally attempted to "concatenate" the video files together, but attempting to play the video, it was "inconsistent" and would often glitch out. I ended up having to reencode all the files (slower), but that made the videos play in a consistent and non-glitched out fashion.
