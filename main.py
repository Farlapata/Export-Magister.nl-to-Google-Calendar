import pdfplumber
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from tqdm import tqdm
import re
from datetime import datetime

# -------------------- CONFIG --------------------
CLIENT_SECRET_FILE = 'credentials.json'  # your OAuth client secret JSON
SCOPES = ['https://www.googleapis.com/auth/calendar']
CALENDAR_ID = 'primary'  # or a specific calendar

# -------------------- OPEN PDF --------------------
Tk().withdraw()
pdf_path = askopenfilename(title="Select your Magister PDF", filetypes=[("PDF files", "*.pdf")])

if not pdf_path:
    print("No PDF selected, exiting.")
    exit()

# -------------------- PARSE PDF --------------------
pages_text = []
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        pages_text.append(page.extract_text())

# Merge lines and normalize
lessons_raw = []
for page_text in pages_text:
    lines = [line.strip() for line in page_text.splitlines() if line.strip()]
    buffer = ""
    for line in lines:
        # Merge lines that start with time range or day
        if re.match(r'\d{2}:\d{2} - \d{2}:\d{2}', line) or re.match(r'\w+dag \d+ \w+', line.lower()):
            if buffer:
                lessons_raw.append(buffer.strip())
            buffer = line
        else:
            buffer += " " + line
    if buffer:
        lessons_raw.append(buffer.strip())

# Dutch months
months = {
    'januari': 1, 'februari': 2, 'maart': 3, 'april': 4,
    'mei': 5, 'juni': 6, 'juli': 7, 'augustus': 8,
    'september': 9, 'oktober': 10, 'november': 11, 'december': 12
}

lessons = []
current_date = None

for line in lessons_raw:
    # Check for date
    date_match = re.match(r'(\w+dag) (\d+) (\w+)', line.lower())
    if date_match:
        day_name, day_num, month_name = date_match.groups()
        month = months.get(month_name, 8)  # default August
        year = datetime.now().year
        current_date = (year, month, int(day_num))
        continue

    # Match lesson line
    lesson_match = re.match(
        r'(\d{2}:\d{2}) - (\d{2}:\d{2})\s+\d+\s+(\w+)\s*-\s*(\w+)\s*-\s*([\w,-]+)\s*(?:\(?([A-Za-z0-9\-]+)?\)?)?',
        line
    )
    if lesson_match and current_date:
        start_time, end_time, subject, teacher, class_name, room = lesson_match.groups()
        year, month, day = current_date
        start_dt = datetime(year, month, day, int(start_time[:2]), int(start_time[3:]))
        end_dt = datetime(year, month, day, int(end_time[:2]), int(end_time[3:]))
        lessons.append({
            'subject': subject,
            'teacher': teacher,
            'class': class_name,
            'room': room if room else "",
            'start': start_dt,
            'end': end_dt
        })

# -------------------- GOOGLE CALENDAR AUTH --------------------
flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
creds = flow.run_local_server(port=0)
service = build('calendar', 'v3', credentials=creds)

# -------------------- ADD EVENTS --------------------
success_count = 0
failed_count = 0

for lesson in tqdm(lessons, desc="Adding lessons"):
    event = {
        'summary': f"{lesson['subject']} ({lesson['class']})",
        'location': lesson['room'],
        'description': f"Teacher: {lesson['teacher']}",
        'start': {'dateTime': lesson['start'].isoformat(), 'timeZone': 'Europe/Amsterdam'},
        'end': {'dateTime': lesson['end'].isoformat(), 'timeZone': 'Europe/Amsterdam'}
    }
    try:
        service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
        success_count += 1
    except Exception as e:
        failed_count += 1
        print(f"Failed to add {lesson['subject']} on {lesson['start'].date()}: {e}")

print("\nFinished!")
print(f"Total lessons found: {len(lessons)}")
print(f"Successfully added: {success_count}")
print(f"Failed to add: {failed_count}")
