# Vid_To_ASCII
Simple script to turn a video into a set of text files containing it as ascii, that can be run from the cmd

# How To Use
Put a video named "video.mp4" in the same directory as the python script. And run it, wait for it to finish converting.
The output will be a bunch of txt files in he folder conversion. Open a terminal in there and run the following command.

```for file in $(ls -v *.txt); do clear; cat "$file"; sleep 0.04; done ```

Do note if the characters look off then you likely have the wrong dimensions of characters in your terminal. 
To get the correct ones run 

```stty size``` 

And set those values in the py script before executing again



Before:
<img width="1916" height="1060" alt="screenshot-2026-11-19_20:40:42" src="https://github.com/user-attachments/assets/c2d59344-42ec-4103-9eca-4bdcc7155bd0" />

After:
<img width="1916" height="1060" alt="screenshot-2026-11-19_20:41:26" src="https://github.com/user-attachments/assets/97fc62e4-5659-4d99-88cc-c337da2a2823" />
