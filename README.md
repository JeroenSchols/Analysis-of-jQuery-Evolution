# Assignment-2-2020
Repository of Group 10 of 2IMP25 Software Evolution Assignment 2

# Scripts
file | purpose
--- | ---
prep.py | Executed on Docker build, clones all analysed versions of jQuery
countLines.py | From within the docker image, counts the code lines of all jQuery releases and outputs them to `out/cloc`
compare.py | From within the docker image, runs JsInspect on any two versions, outputting to `out/return`
process.py | From outside the docker image, uses JsInspect and Cloc results of the `jQuery-comparisons` and `jQuery-linecounts` folders respectively to compute similarity and call the visualization script  
visualization.py | Contains code for generating the heatmap and barchart
manual-clones | folder containing all constructed manual clones for testing of JsInspect

# Dockerfile

The docker file sets up a docker image where three things 
are prepared:
- JsInspect is installed, such that you can run it from the 
command line.
- Cloc is installed.
- All versions of jQuery specified in `jquery_releases.csv` are 
cloned and downloaded to `/usr/jquery-data`.
- manual-clones folder is available within the container
- countLines.py and compare.py can be executed

When running the container a bash shell is opened such that you
can manually execute commands to run JsInspect and cloc. 

## Using this image

Build using `docker build -t 2imp25-assignment-2 ./`

Then run using 
Windows (Powershell): `docker run -it --rm -v "$PWD\out:/out" 2imp25-assignment-2`
Linux: `docker run -it --rm -v "$PWD/out:/out" 2imp25-assignment-2`. 
We again mount an out directory linked to the host file system
such that you can copy out files from the container. 

When the container is running you can execute bash commands
as if it is a virtual machine. 

To receive pairwise comparisons execute compare.py in the /usr folder.