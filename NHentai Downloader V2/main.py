import requests, os, json
from bs4 import BeautifulSoup

class Main:
    def Downloader(id:int=None):
        with open("./Cookies.json", "r") as cookiesInput:
            cookiesJson = json.loads(cookiesInput.read())

            if cookiesJson["csrftoken"] == "" or cookiesJson["cf_clearance"] == "":
                print("Please insert a cookie ...")
            else:
                cookies = {
                    'csrftoken': cookiesJson["csrftoken"],
                    'cf_clearance': cookiesJson["cf_clearance"]
                }

                headers = {
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
                }

                response = requests.get(f"https://nhentai.net/g/{str(id)}", cookies=cookies, headers=headers)
                soup = BeautifulSoup(response.text, "html.parser")
                pages = soup.find_all("a", {"class":"gallerythumb"})

                for i in pages:
                    response = requests.get(f"https://nhentai.net/{i['href']}", cookies=cookies, headers=headers)
                    soup = BeautifulSoup(response.text, "html.parser")
                    img = soup.find_all("img")[1]["src"]
                    file_name = img.split("/")
                    response = requests.get(img, cookies=cookies, headers=headers)

                    if (os.path.isdir(f"./{idInput}")):
                        with open(f"./{idInput}/{file_name[5]}", "wb") as output:
                            output.write(response.content)
                            print(file_name[5] + " - Done!")
                    else:
                        os.makedirs(f"./{idInput}")
                        with open(f"./{idInput}/{file_name[5]}", "wb") as output:
                            output.write(response.content)
                            print(file_name[5] + " - Done!")
                print("Operation Done!")
                
if __name__ == "__main__":
    os.system("cls")
    while True:
        try:
            idInput = int(input("NHentai ID: "))
            if idInput == "":
                print("Please insert an ID ...")
            else:
                    Main.Downloader(idInput)
        except Exception as error:
            print(str(error))