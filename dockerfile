FROM python:3.10-slim as req-instalation

#Requrements instalation to venv
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install -r requirements.txt

FROM req-instalation as build-image

# Coppy project files
COPY . .

# Coppy venv

COPY --from=req-instalation /venv /venv

# Activate coppyed venv
ENV PATH="/venv/bin:$PATH"

CMD ["python", "main.py"]