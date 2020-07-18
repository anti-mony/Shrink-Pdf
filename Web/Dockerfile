FROM python:3.8.4-alpine3.12

# Set work directory
WORKDIR /usr/src/app

# Install dependencies
RUN apk add ghostscript --no-cache
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# Copy project
COPY . /usr/src/app/

# Change the cron job according to your needs
# Add Auto Delete Cron Job
COPY ./cleardata.sh /etc/periodic/hourly/
