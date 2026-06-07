import requests
import time
import signal
import sys

URL = "https://zeros-a64a9-default-rtdb.firebaseio.com/chat/messages.json"

running = True
print("لكي تتمكن من ارسال رسائل استخدم هاذا الكود في أنظمة لينوكس")
print("""curl -X POST \
-H "Content-Type: application/json" \
-d '{
  "name": "zero",
  "message": "hello zeros"
}' \
"https://zeros-a64a9-default-rtdb.firebaseio.com/chat/messages.json"
""")
# إيقاف البرنامج عند Ctrl + X أو Ctrl + C
def stop_signal(sig, frame):
    global running
    print("\nتم إيقاف البرنامج")
    running = False
    sys.exit(0)

signal.signal(signal.SIGINT, stop_signal)

last_data = {}

def fetch_messages():
    try:
        r = requests.get(URL)
        return r.json()
    except:
        return None

print("بدء مراقبة الرسائل...")

while running:
    data = fetch_messages()

    if data:
        # طباعة الرسائل الجديدة فقط
        for key, msg in data.items():
            if key not in last_data:
                print(f"{msg.get('name')} : {msg.get('message')}")
                last_data[key] = msg

    time.sleep(2)



