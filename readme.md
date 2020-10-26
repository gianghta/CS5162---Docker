# Docker Assignment (CS5165 - Cloud Computing)

A small python script that runs in a container and:
- Display all current files in /home/data
- Read all .txt files, count how many words each have and display the amount
- Display the file with largest number of words and total words in every files
- Find the IP address of the machine and host name
- Save all results into `/home/output/result.txt`
- Read from `/home/output/result.txt` and print out content when container starts

### Build the image and run the container
- Run `docker build -t <tag name> .` to build the image
- Run `docker run <tag name>` to run the container
- Container runs and shows all the infos from **result.txt** that was written in.

### View structure of the container
- Run `docker save <tag name> > <name>.tar` to create .tar file to view the container structures
- There's also a .tar file included in this repository for use