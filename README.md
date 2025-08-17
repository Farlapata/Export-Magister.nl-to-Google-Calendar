# Magister to Google Calendar Exporter

[![GitHub stars](https://img.shields.io/github/stars/YOURUSERNAME/Magister-to-Google-Calendar?style=for-the-badge)](https://github.com/YOURUSERNAME/Magister-to-Google-Calendar/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/YOURUSERNAME/Magister-to-Google-Calendar?style=for-the-badge)](https://github.com/YOURUSERNAME/Magister-to-Google-Calendar/network/members)
[![GitHub issues](https://img.shields.io/github/issues/YOURUSERNAME/Magister-to-Google-Calendar?style=for-the-badge)](https://github.com/YOURUSERNAME/Magister-to-Google-Calendar/issues)
[![License](https://img.shields.io/github/license/YOURUSERNAME/Magister-to-Google-Calendar?style=for-the-badge)](LICENSE)

---

## 🌟 Features

- Extracts lessons from Magister PDF files
- Handles Dutch dates and months
- Adds events to Google Calendar with subject, class, teacher, and room
- Simple GUI to select PDF
- Real-time progress bar and error reporting

---

## 🛠️ Built With

- **Python 3.8+**
- **pdfplumber** – PDF parsing
- **tkinter** – File dialog GUI
- **google-auth-oauthlib** – Google OAuth authentication
- **google-api-python-client** – Google Calendar API
- **tqdm** – Progress bars

---

## ⚙️ Installation

```bash
pip install pdfplumber google-auth-oauthlib google-api-python-client tqdm
```

---

## 📝 Setup Guide

### 1️⃣ Export Magister PDF

1. Log in to [Magister.nl](https://www.magister.nl).
2. Navigate to your **schedule/agenda**.
3. Click **Afdrukken** (Print) to export the timetable.
4. **Important:** Only one week is exported at a time. Repeat for each week you want to add.
5. Save the PDF to a known location on your computer.

---

### 2️⃣ Google Calendar API Setup

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a **new project** or select an existing project.
3. In the left sidebar, click **APIs & Services → Library**.
4. Search for **Google Calendar API** and click **Enable**.
5. After enabling, navigate to **APIs & Services → Credentials**.
6. Click **Create Credentials → OAuth client ID**.
7. If prompted to configure the consent screen:
   - Select **External** for personal use.
   - Fill in **App Name**, **User Email**, and **Scopes** (you can leave optional info blank).
   - Save the consent screen configuration.
8. Back at **Create OAuth Client ID**, choose **Desktop App**.
9. Give it a name (like `Magister Calendar Exporter`) and click **Create**.
10. Download the JSON file. This is your `credentials.json`.  
11. **Important:** Move `credentials.json` into the same folder as `magister_to_calendar.py`.

---

### 3️⃣ Verify Setup

1. Make sure Python 3.8+ is installed.
2. Install required packages:

```bash
pip install pdfplumber google-auth-oauthlib google-api-python-client tqdm
```

3. Confirm `credentials.json` is in the project folder.
4. Your project folder should now contain:
   ```
   magister_to_calendar.py
   credentials.json
   ```
5. You are ready to run the script.

---

## 🚀 Usage

```bash
python magister_to_calendar.py
```

1. Select the Magister PDF when prompted.
2. Authenticate with Google Calendar via the browser window.
3. Lessons will be automatically added to your calendar.

---

## 💡 Notes

- One PDF = **one week**; run separately for each week.
- Default timezone is **Europe/Amsterdam**. Change in the script if needed.
- Events include subject, class, teacher, and room.

---

## ❌ Troubleshooting

- **Failed to add events:** Make sure the PDF format is correct.
- **Authentication issues:** Verify `credentials.json` and API setup.
- **Dependencies:** Ensure Python packages are installed.

---

## ⭐ Support & Contributions

If you like this project, please **star ⭐ it**, **watch 👀 it**, or **fork 🍴 it**!

[![Star](https://img.shields.io/badge/Star-⭐-brightgreen?style=for-the-badge)](https://github.com/YOURUSERNAME/Magister-to-Google-Calendar/stargazers)
[![Fork](https://img.shields.io/badge/Fork-🍴-blue?style=for-the-badge)](https://github.com/YOURUSERNAME/Magister-to-Google-Calendar/fork)
[![Report Issue](https://img.shields.io/badge/Report%20Issue-🐛-red?style=for-the-badge)](https://github.com/YOURUSERNAME/Magister-to-Google-Calendar/issues)

---

## 📜 License

MIT License – see the [LICENSE](LICENSE) file.
