import smtplib
import time
import random
from email.mime.text import MIMEText

# 🔐 Sender
sender_email = "mogiliakash7@gmail.com"
password = "yshliwadezqmybkw"

# 👥 Multiple receivers
receivers = [
    "b23159@students.iitmandi.ac.in",
    "veeraswamymogili34@gmail.com"
]

# 💬 Random messages
messages = [
    
    [
        "Good morning! 🌞 Stay focused and keep learning!",
        "Every small step matters.",
        "Don’t wait for motivation — create it.",
        "Keep your goals in sight.",
        "Make today count! 🚀"
    ],
    
    [
        "Rise and shine! 💪 Today is a new opportunity!",
        "Your effort defines your future.",
        "Stay disciplined.",
        "Avoid distractions.",
        "You’ve got this! 🔥"
    ],
    
    [
        "Good morning! 🌅 A fresh start awaits you.",
        "Consistency is your biggest strength.",
        "Keep pushing forward.",
        "Learn something new today.",
        "Stay unstoppable! 🚀"
    ],
    
    [
        "Start your day with purpose! 📚",
        "Focus on what matters.",
        "Ignore noise, build value.",
        "Progress over perfection.",
        "Keep growing! 🌱"
    ],
    
    [
        "Consistency beats motivation. 🔥",
        "Show up even when it’s hard.",
        "Discipline builds success.",
        "Stay committed.",
        "Win your day! 💯"
    ],
    
    [
  
        "Good morning! 🌞 Time to build your future.",
        "Start before you feel ready.",
        "Action beats planning.",
        "Push your limits.",
        "Make it happen! 🚀"
    ],
    
    [
        "Wake up with determination! 💪",
        "Focus deeply.",
        "Work quietly.",
        "Let results speak.",
        "Stay strong! 🔥"
    ],
    
    [
        "A new day, a new chance! 🌅",
        "Learn. Build. Repeat.",
        "Stay consistent.",
        "Trust the process.",
        "Keep moving! 🚀"
    ],
    
    [
        "Good morning! 🌞 Be intentional today.",
        "Set clear goals.",
        "Avoid time waste.",
        "Stay sharp.",
        "Execute well! 💯"
    ],
    
    [
        "Rise up! 🔥 Today matters.",
        "Push beyond comfort.",
        "Stay focused.",
        "Be disciplined.",
        "Achieve something meaningful! 🚀"
    ],
    
    [
        "Good morning! 🌞 Stay committed today.",
        "Focus on your priorities.",
        "Avoid unnecessary distractions.",
        "Work with intention.",
        "Make progress! 🚀"
    ],
    
    [
        "Rise and shine! 🌅 Build your momentum.",
        "Start small but start now.",
        "Stay consistent.",
        "Keep learning.",
        "Finish strong! 💯"
    ],
    
    [
        "Good morning! 💪 Take control of your day.",
        "Plan wisely.",
        "Execute effectively.",
        "Stay disciplined.",
        "Achieve more! 🔥"
    ],
    
    [
        "A fresh morning awaits! 🌞",
        "Think clearly.",
        "Act confidently.",
        "Stay focused.",
        "Win your goals! 🚀"
    ],
    
    [
        "Good morning! 🌅 Time to grow.",
        "Push your limits.",
        "Embrace challenges.",
        "Stay positive.",
        "Keep moving forward! 💪"
    ],
    
    [
        "Wake up and take action! 🔥",
        "Your future depends on today.",
        "Focus deeply.",
        "Stay consistent.",
        "Make it happen! 🚀"
    ],
    
    [
        "Good morning! 🌞 Stay sharp.",
        "Be proactive.",
        "Stay productive.",
        "Avoid delays.",
        "Keep going strong! 💯"
    ],
    
    [
        "Rise and grind! 💪",
        "Your effort matters.",
        "Keep pushing.",
        "Stay committed.",
        "Achieve greatness! 🚀"
    ],
    
    [
        "Good morning! 🌅 Stay determined.",
        "Focus on your path.",
        "Ignore distractions.",
        "Work with purpose.",
        "Keep improving! 🔥"
    ],
    
    [
        "Start your day right! 🌞",
        "Think big.",
        "Act small.",
        "Stay consistent.",
        "Grow daily! 🚀"
    ],
    
    [
        "Good morning! 💯 Be unstoppable.",
        "Keep learning.",
        "Keep building.",
        "Stay focused.",
        "Win today! 🔥"
    ],
    
    [
        "Rise up! 🌅 Take charge.",
        "Start strong.",
        "Stay focused.",
        "Finish well.",
        "Achieve more! 🚀"
    ],
    
    [
        "Good morning! 🌞 Stay ahead.",
        "Think clearly.",
        "Work smart.",
        "Stay disciplined.",
        "Keep winning! 💪"
    ],
    
    [
        "Wake up and shine! ✨",
        "Plan your day.",
        "Act with purpose.",
        "Stay sharp.",
        "Make impact! 🚀"
    ],
    
    [
        "Good morning! 🌅 Focus matters.",
        "Stay intentional.",
        "Avoid noise.",
        "Keep building.",
        "Move forward! 💯"
    ],
    
    [
        "Rise and shine! 🌞 Be ready.",
        "Stay active.",
        "Stay focused.",
        "Stay disciplined.",
        "Achieve success! 🔥"
    ],
    
    [
        "Good morning! 💪 Build habits.",
        "Stay consistent.",
        "Push limits.",
        "Stay strong.",
        "Win daily! 🚀"
    ],
    
    [
        "Start fresh! 🌅 New opportunities.",
        "Take action.",
        "Stay focused.",
        "Keep growing.",
        "Make progress! 💯"
    ],
    
    [
        "Good morning! 🌞 Stay positive.",
        "Think clearly.",
        "Act boldly.",
        "Stay consistent.",
        "Keep improving! 🚀"
    ],
    
    [
        "Rise up! 💪 Stay focused.",
        "Avoid distractions.",
        "Work deeply.",
        "Stay committed.",
        "Achieve goals! 🔥"
    ],
    
    [
        "Good morning! 🌅 Be focused.",
        "Start early.",
        "Stay sharp.",
        "Work hard.",
        "Finish strong! 🚀"
    ],
    
    [
        "Wake up! 🌞 Stay productive.",
        "Think smart.",
        "Act wisely.",
        "Stay disciplined.",
        "Keep going! 💯"
    ],
    
    [
        "Good morning! 💪 Stay determined.",
        "Push forward.",
        "Stay focused.",
        "Work consistently.",
        "Achieve success! 🚀"
    ],
    
    [
        "Rise and shine! 🌅 Build momentum.",
        "Start now.",
        "Stay consistent.",
        "Keep learning.",
        "Grow daily! 🔥"
    ],
    
    [
        "Good morning! 🌞 Take action.",
        "Avoid delay.",
        "Stay focused.",
        "Work smart.",
        "Make progress! 🚀"
    ],
    
    [
        "Start strong! 💪 Stay committed.",
        "Think clearly.",
        "Act boldly.",
        "Stay disciplined.",
        "Win today! 💯"
    ],
    
    [
        "Good morning! 🌅 Stay sharp.",
        "Be focused.",
        "Work smart.",
        "Stay consistent.",
        "Keep growing! 🚀"
    ],
    
    [
        "Rise up! 🌞 Stay ahead.",
        "Think big.",
        "Act now.",
        "Stay consistent.",
        "Achieve more! 🔥"
    ],
    
    [
        "Good morning! 💪 Stay strong.",
        "Focus deeply.",
        "Avoid distractions.",
        "Work consistently.",
        "Make progress! 🚀"
    ],
    
    [
        "Wake up! 🌅 New day.",
        "New goals.",
        "Stay focused.",
        "Stay disciplined.",
        "Win today! 💯"
    ],
    
    [
        "Good morning! 🌞 Be productive.",
        "Plan well.",
        "Execute well.",
        "Stay focused.",
        "Achieve success! 🚀"
    ],
    
    [
        "Rise and shine! 💪 Stay committed.",
        "Focus clearly.",
        "Act wisely.",
        "Stay disciplined.",
        "Make impact! 🔥"
    ],
    
    [
        "Good morning! 🌅 Stay motivated.",
        "Push forward.",
        "Stay consistent.",
        "Work smart.",
        "Grow daily! 🚀"
    ],
    
    [
        "Start your day! 🌞 Stay focused.",
        "Think clearly.",
        "Act boldly.",
        "Stay consistent.",
        "Win today! 💯"
    ],
    [
    
        "Good morning! 💪 Stay sharp.",
        "Focus deeply.",
        "Avoid noise.",
        "Stay consistent.",
        "Achieve more! 🚀"
    ],
    
    [
        "Rise up! 🌅 Be productive.",
        "Plan smart.",
        "Act fast.",
        "Stay disciplined.",
        "Make progress! 🔥"
    ],
    
    [
        "Good morning! 🌞 Stay active.",
        "Think clearly.",
        "Work smart.",
        "Stay consistent.",
        "Win daily! 🚀"
    ],
    
    [
        "Wake up! 💪 Stay focused.",
        "Avoid distractions.",
        "Stay consistent.",
        "Work hard.",
        "Achieve success! 💯"
    ],
    
    [
        "Good morning! 🌅 Stay determined.",
        "Push limits.",
        "Stay strong.",
        "Work consistently.",
        "Grow daily! 🚀"
    ],
    
    [
        "Rise and shine! 🌞 Stay sharp.",
        "Think clearly.",
        "Act wisely.",
        "Stay focused.",
        "Make progress! 🔥"
    ],
    
    [
        "Good morning! 💪 Stay committed.",
        "Focus deeply.",
        "Stay consistent.",
        "Work smart.",
        "Win today! 🚀"
    ],
    
    [
        "Start fresh! 🌅 Stay positive.",
        "Think clearly.",
        "Act boldly.",
        "Stay focused.",
        "Grow daily! 💯"
    ],
    
    [
        "Good morning! 🌞 Stay productive.",
        "Plan wisely.",
        "Execute well.",
        "Stay disciplined.",
        "Achieve success! 🚀"
    ],
    
    [
        "Rise up! 💪 Stay focused.",
        "Avoid noise.",
        "Work deeply.",
        "Stay consistent.",
        "Make impact! 🔥"
    ],
    
    [
        "Good morning! 🌅 Stay strong.",
        "Push forward.",
        "Stay focused.",
        "Work consistently.",
        "Win today! 🚀"
    ],
    
    [
        "Wake up! 🌞 Stay active.",
        "Think smart.",
        "Act wisely.",
        "Stay consistent.",
        "Achieve more! 💯"
    ],
    
    [
        "Good morning! 💪 Stay disciplined.",
        "Focus clearly.",
        "Stay consistent.",
        "Work hard.",
        "Grow daily! 🚀"
    ],
    
    [
        "Rise and shine! 🌅 Stay sharp.",
        "Think clearly.",
        "Act boldly.",
        "Stay focused.",
        "Win today! 🔥"
    ],
    
    [
        "Good morning! 🌞 Stay determined.",
        "Push forward.",
        "Stay consistent.",
        "Work smart.",
        "Make progress! 🚀"
    ],
    
    [
        "Start strong! 💪 Stay focused.",
        "Think clearly.",
        "Act wisely.",
        "Stay disciplined.",
        "Achieve success! 💯"
    ]

]
# ⏰ Random delay (0–120 minutes)
delay = random.randint(0, 120 * 60)
print(f"⏳ Waiting for {delay//60} minutes...")
time.sleep(delay)

# 🎯 Pick random message set
selected_set = random.choice(messages)
body = "\n".join(selected_set)

subject = "🌅 Good Morning!"

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)

    for receiver in receivers:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = receiver

        server.sendmail(sender_email, receiver, msg.as_string())
        print(f"✅ Sent to {receiver}")

    server.quit()

except Exception as e:
    print("❌ Error:", e)
