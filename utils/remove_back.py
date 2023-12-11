import requests

url = "https://background-removal.p.rapidapi.com/remove"


async def background_remove(image):
    payload = {"image_url": f"{image}"}
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "0e1e80d5bfmsh213ed89c8e67ef5p10d6b3jsn0c4cbb51f1b1",
        "X-RapidAPI-Host": "background-removal.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)
    print(response.json())
    return response.json()['response']['image_url']
