FROM jupyter/base-notebook:python-3.8

# Set working direction
WORKDIR /home/jovyan

COPY new_requirements.txt new_requirements.txt

#RUN pip install -r requirement.txt
RUN pip install --upgrade pip && pip install -r new_requirements.txt