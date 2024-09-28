import requests
import os

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {
    'sol': 1001,
    'camera': 'fhaz',
    'api_key': 'DEMO_KEY'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    photos = data.get('photos', [])

    if not photos:
        print("No photos are available for the specified parameters.")
    else:

        for idx, photo in enumerate(photos, start=1):
            img_url = photo['img_src']
            print(f"Uploading a photo {idx}: {img_url}")


            img_data = requests.get(img_url).content


            img_name = f"mars_photo{idx}.jpg"
            with open(img_name, 'wb') as file:
                file.write(img_data)

            print(f"Photo {idx} saved as {img_name}")

        print(f"Downloaded and saved {len(photos)} photo.")
else:
    print(f"Unable to retrieve data. Status: {response.status_code}")