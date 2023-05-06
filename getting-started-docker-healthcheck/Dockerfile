FROM python:3.11-bullseye

RUN pip install --no-cache-dir Flask==2.2.3

COPY app.py /

EXPOSE 5000

# Check whether the app is running
HEALTHCHECK --interval=3s --timeout=2s \
    CMD curl --silent --fail http://localhost:5000/ping || exit 1

# Run the Flask application and make it listen on any interface
CMD ["flask", "run", "--host=0.0.0.0"]