
FROM python:3.9
WORKDIR .
ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
COPY startup.sh .
RUN bash startup.sh
COPY . .
EXPOSE 200
RUN npm start
CMD ["bash", "step.sh"]
EXPOSE 3000
