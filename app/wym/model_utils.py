import requests

base_url = 'http://model:5000/model/predict'
test_json = {
  "text": [
    "string"
  ]
}

def summarize(text:str):
    json = {}
    json['text'] = [text]

    r = requests.post(
        url = base_url,
        json = json
    ).json()
    print(f'Response {r}')
    if r['status'] == 200:
      print(r['summary_text'])
      summary = r['summary_text']
    elif r['status'] == 400:
      summary = 'BAD REQUEST'

    summary = r['summary_text']
    return summary

if __name__ == '__main__':
    print('Test de Requests et text summary')
    r = requests.post(
        url = base_url,
        json = test_json
    )
    print(r.json()['status'])
    print(r.json()['summary_text'])