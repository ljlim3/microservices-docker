# microservices-docker

1. Clone this repository
2. In terminal, install socat: “brew install socat”
3. Start socat as follows: socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\"
4. Open a new tab in your terminal
5. In terminal, cd into the directory where the repository folder is saved
6. In docker-compose.yml, replace DISPLAY variable values on the left-hand side of the colon to your own IP address. (The DISPLAY variable is required for the “git” and “data-science-toolbox” services.)
7. Run “docker-compose up” command in the terminal
8. Go to localhost:5000, which is the main app (the Data Science Toolbox)
Note: For Apache Spark (pyspark): On the top right of the Jupiter notebook, click New and create a new Python3 notebook. Import pyspark as follows: “import pyspark”. You can now start using pyspark.
Note: For TensorFlow and Apache Spark, copy the tokens from the terminal. 
Note: Git will open up automatically upon build.
12. Run ctrl-C to exit the program.


Recording: https://youtu.be/u3wqcgM6zyI
