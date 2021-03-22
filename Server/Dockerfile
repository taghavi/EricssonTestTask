# Just a remember, dockerfile must always start by importing the base image.
# We use the keyword 'FROM' to do that.
# In our example, we want to import the python image (from DockerHub).
# So, we write 'python' for the image name and 'latest' for the version.
#FROM python:latest

# In order to launch our python code, we must import the 'server.py' and 'index.html' file.
# We use the keyword 'ADD' to do that.
# Just a remember, the first parameter 'server.py' is the name of the file on the host.
# The second parameter '/server/' is the path where to put the file on the image.
# Here we put files at the image '/server/' folder.
#ADD server.py /server/


# I would like to introduce something new, the 'WORKDIR' command.
# This command changes the base directory of your image.
# Here we define '/server/' as base directory (where all commands will be executed).
#WORKDIR /server/

# FROM python:3.7.5-slim
# RUN python -m pip install \
#         parse \
#         realpython-reader
# Set up and activate virtual environment
# ENV VIRTUAL_ENV "../../Desktop/Thesis/python/.venv"
# RUN python -m .venv $VIRTUAL_ENV
# ENV PATH "$VIRTUAL_ENV/bin:$PATH"

# FROM python:latest

# ADD server.py /
# WORKDIR /

# ENTRYPOINT ["python","/server.py"]

FROM python:latest
ENV HOSTNAME server_test_task
COPY . app/
WORKDIR /app
EXPOSE 9980
RUN pip3 install -r requirements.txt
COPY . /
CMD ["python","/app/server.py"]
# CMD ["/server.py"]
# ENTRYPOINT ["python"]
