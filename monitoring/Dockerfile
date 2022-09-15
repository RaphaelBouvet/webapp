FROM python:3.8.10
WORKDIR /monitoring
COPY ./requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD streamlit run monitoring/dashboard.py
