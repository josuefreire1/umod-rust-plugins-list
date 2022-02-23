import requests
import time
import os.path

#url = "https://umod.org/plugins/search.json?query=&page=1&sort=downloads&sortdir=desc&filter=&categories%5B%5D=rust&author="
#scraper = cloudscraper.create_scraper()
#html = scraper.get(url).text
#page_soup = soup(html, "html.parser")
#
#site_json=json.loads(page_soup.text)
#
#print(site_json['watchers'])
save_path = 'C:/Users/Unicorn/Desktop/plugins scraper/plugins/'
i=1
tag = "broken"
while i <= 130:
    url = "https://umod.org/plugins/search.json?query=&page="+ str(i) +"&sort=downloads&sortdir=desc&filter=&categories%5B%5D=rust&author="
    
    
    #all_data = requests.get(url).json()
    
    
    response=requests.get(url)
    while response.status_code == 429:
        print("Ah ah ah, you didn't say the magic word")
        #print(response.content)
        #print(response.headers)
        time.sleep(30)
        response=requests.get(url)

    all_data = response.json()

    #-------------------------------------------------------------------------------------------------
#Write to file
    f=open("plugins.txt", "a+", encoding="utf-8")
    f.write("====================Page"+ str(i) +"================================\n\n")
    f.close()
    print("====================Page"+ str(i) +"================================\n\n")
    for plugin  in all_data['data']:
        f=open("plugins.txt", "a+", encoding="utf-8")

        if tag in plugin['tags_all']:
            print('Titulo:' + plugin['title'] + 'BROKEN')
            #Write to file
            f.write('Titulo:' + plugin['title'] + 'BROKEN\n')
            f.write(plugin['download_url'] + '\n')
            f.write('----------------------------------------------------------------------------\n')
            f.close()
            
        else:
            print('Titulo:' + plugin['title'] + ' ||Desc.:' + plugin['description'])
            print(plugin['download_url'])
            print(plugin['tags_all'])

            #Write to file
            f.write('Titulo:' + plugin['title'] + ' ||Desc.:' + plugin['description'] + '\n')
            f.write(plugin['tags_all'] + '\n')
            f.write(plugin['download_url'] + '\n')
            f.write('----------------------------------------------------------------------------\n')
            f.close()

            #Download part
            download_link = plugin['download_url']
            name = plugin['name']
            file = os.path.join(save_path, name + ".cs")
            r = requests.get(download_link, allow_redirects=True)
            while r.status_code == 429:
                print("Ah ah ah Download failed")
                print(download_link)
                #print(response.headers)
                time.sleep(30)
                r=requests.get(download_link, allow_redirects=True)
            open(file, 'wb').write(r.content)
        #time.sleep(2)
        
    i += 1
    
