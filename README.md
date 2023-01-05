## NHentai Downloader V2
[![image](https://img.shields.io/github/v/release/Charlzk05/NHentai-Downloader-V2)](https://github.com/Charlzk05/NHentai-Downloader-V2/releases/tag/v1.0.0)

A NHentai Downloader that uses cookies to bypass "nhentai.net" cloudflare

### Installation

1. Download or clone the repository `git clone https://github.com/Charlzk05/NHentai-Downloader-V2.git`
2. Install requirements `pip install -r requirements.txt`

- Enjoy

## How to use

1. Insert your nhentai.net cookies first on `Cookies.json`
   - Json Format
   ```json
   {
     "cf_clearance": "<Your cf_clearance cookie>",
     "csrftoken": "<Your csrftoken cookie>",
     "userAgent": "<Your user-agent identify>"
   }
   ```
2. Run the program `main.py`
3. Insert your nhentai id that you want to download
4. Enjoy!

### Result

![Screenshot 2022-10-31 171043](https://user-images.githubusercontent.com/104715127/198975722-bf91294b-ac35-47ef-97e7-9f098ba99697.png)

## How to get your nhentai cookie and user-agent

1. Go to "nhentai.net" website
2. View site information or the lock icon on the address bar

   ![image](https://user-images.githubusercontent.com/104715127/198975166-d24a9a0c-a722-46cc-a707-b30fe08917cd.png)
   
3. Click "cookies"
4. Navigate to your cookies `nhentai.net > Cookies`

   ![image](https://user-images.githubusercontent.com/104715127/198975400-c035d020-641a-4d45-ae69-d1d720589c47.png)

5. Open your Developer Tools or press `f12` and go to "Console" tab and paste this code

   ```js
   // Copy your user-agent automatically to clipboard
   copy(navigator.userAgent)
   ```
   ![image](https://user-images.githubusercontent.com/113793173/210773239-f153f2ad-16f5-40d9-a60d-57df6b28a507.png)

6. Enjoy

### Packages used
- Requests
- BeautifulSoup
