FROM <image>:<tag>

WORKDIR <path>

# Install dependencies
COPY <file/host path> <working directory>
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY <file/host path> <working directory>

EXPOSE <port number>

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]