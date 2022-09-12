import requests

base_url = 'http://0.0.0.0:5000/model/predict'
test_json = {
  "text": [
    "string"
  ]
}

if __name__ == '__main__':
    print('Test de Requests et text summary')
    r = requests.post(
        url = base_url,
        json = test_json
    )
    print(r.json()['status'])
    print(r.json()['summary_text'])