from db_transfer.file_transfer import send_file

# Usage
filename = 'data/main.db'  # replace with your file name
url = 'http://127.0.0.1:8000/'  # replace with your URL
response = send_file(filename, url)
print(response.status_code)

