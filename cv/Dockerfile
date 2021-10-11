FROM python:3.8

RUN pip install WeasyPrint

RUN useradd -ms /bin/bash maker
USER maker
WORKDIR /home/maker

# ADD cv_maker cv_maker

CMD python cv_maker/generate_cv.py
