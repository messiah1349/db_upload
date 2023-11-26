import requests

def send_file(filename, url):
    # Open the file in binary mode
    # with open(filename, 'rb') as f:
    #     # Read the file
    #     file_data = f.read()

    file_data = {'file': open(filename, 'rb')}

    # Send the file data as a POST request
    response = requests.post(url=url, files=file_data)

    print(response.json())

    return response

