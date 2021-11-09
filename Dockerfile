FROM python:3.8.6 AS base


FROM base AS lint

RUN pip install black

WORKDIR /data
ENTRYPOINT ["black"]


FROM base AS dependencies

COPY requirements.txt .
RUN pip install -r requirements.txt


FROM dependencies AS build

COPY . .

ENTRYPOINT [ "python", "setup.py", "install" ]


FROM dependencies as test

COPY test-requirements.txt . 
RUN pip install -r test-requirements.txt

COPY . .

ENTRYPOINT ["python", "-m", "unittest", "discover", "test/"]