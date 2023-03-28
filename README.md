

Go ahead and go out to install docker: https://docs.docker.com/get-docker/

Once you have that installed, you should be able to run something like `docker version` and get some feedback.

Now, download this repository locally to your computer, using something like `git clone https://github.com/mwrolstad/example_airflow`

Once that's done, you can pop into the new project you just downloaded and run the following commands:

- `docker-compose up airflow-init`: this creates the airflow environment for you
- `docker-compose up`: this basically boots a local version of Airflow for you, it may take a few minutes to load.
- Once that is complete, you may see a login page at http://localhost:8080/, the default username and password are `airflow` and `airflow`
- The DAG `my_dag` should be visible to you, and you should be able to run it!
- Just open it up and press the "play" button in the upper right corner.

The full walkthrough is here: https://betterprogramming.pub/how-to-start-running-apache-airflow-in-docker-6567d8165653

Now that you have a DAG working, you should be able to drop your python file into your DAGs folder and run it, or you can also set an environment variable to point to where it is on your teammate's server.

Note, when you're testing it using Docker, you'll need to make sure the files you want to run are locally stored in your Docker container, that means you'll either want to place them in the `plugins` folder and run from there while testing, or you can also "map" them using the `docker-compose` file by adding a volume.