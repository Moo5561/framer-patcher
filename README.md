# framer-patcher
Patches Framer websites to remove branding.

### Tutorial
Have you ever wanted to make a website without code using framer but can't stand that it has a paywall to remove branding?
No?
Well I'm gonna tell you how to remove it anyway!

# How to use this

## 1. Get your Framer files
* Go to Framer and publish your website to a free `.framer.app` domain.
* Head over to a free web scraper like `saveweb2zip.com` (or use your own scraper setup).
* Paste your live link, download the ZIP file, and extract it.

## 2. Setup your directory
Move the extracted website files into the root folder of this repository. It should look like this:

📁 framer-patcher/
├── 📄 config.txt
├── 📄 patcher.py
├── 📄 README.md
└── [Your extracted website files, index.html, assets, etc.]

## 3. Edit config.txt
Open `config.txt` and change the settings to match your site.

name="My Epic Portfolio"
favicon="favicon.ico"

## 4. Run the patcher
Open your terminal in the repository folder and run:

python patcher.py

This will automatically look through all the HTML files in the folder, inject the custom style override to hide the branding badge, update your site's tab title, and swap the favicon to your custom image.

## 5. Deploy
Now you can upload your clean, watermark-free files straight to GitHub Pages, Vercel, Netlify, or whatever hosting platform you want.
