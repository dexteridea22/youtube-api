FROM continuumio/miniconda3:latest

WORKDIR /youtube-video-api

COPY environment.yml /youtube-video-api/environment.yml

COPY . /youtube-video-api/

RUN conda env create -f environment.yml

ENV PATH /opt/conda/envs/youtube/bin:$PATH

CMD ["bash", "-c", "source activate youtube  && python wsgi.py "]
EXPOSE 5000
