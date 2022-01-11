import pandas as pd

url = []
for i in range(0, 1260, 30):
    hotel = f'https://www.tripadvisor.com/Hotels-g303946-oa-{i}-Vung_Tau_Ba_Ria_Vung_Tau_Province-Hotels.html'
    url.append(hotel)
    
url = pd.DataFrame(url)

url.to_csv('Hotel_Vungtau_url.csv')

