import requests
import sys
file_path = sys.argv[1]
response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open(file_path, 'rb')},
    data={'size': 'auto'},
    headers={'X-Api-Key': 'oEEG1Lf2S6tUiZboKfMTyd6L'},
)
#remember to register the API key on the website
#one API key can only test 50 times, or will be charged the fee
if response.status_code == requests.codes.ok:
    with open('Desktop/no-bg.png', 'wb') as out:
        out.write(response.content)
else:
    print("Error:", response.status_code, response.text)