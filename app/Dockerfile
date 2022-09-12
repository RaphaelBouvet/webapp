FROM python:3.8.10

# COPY the wheel
COPY dist /wheel
RUN pip install wheel/wym-0.1.0-py3-none-any.whl

WORKDIR /app
# COPY the script
COPY wym /app/

# RUN the script
CMD python app.py