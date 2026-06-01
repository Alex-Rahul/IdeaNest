from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# ✅ Predefined responses
default_texts = [
    "Welcome to IdeaNest!",
    "IdeaNest helps you manage startup ideas.",
    "You can submit, track, and analyze ideas.",
    "It has dashboards for insights.",
    "You can collaborate with teammates.",
    "Analytics show idea performance.",
    "Notifications keep you updated.",
    "AI assistant gives suggestions.",
    "Reports summarize your progress.",
    "Settings let you customize your workspace."
]

@csrf_exempt
def chatbot_view(request):
    messages = []
    if request.method == "POST":
        user_message = request.POST.get("message", "").lower()
        messages.append({"sender": "user", "text": user_message})

        # ✅ Rule-based responses
        if user_message == "hi":
            ai_reply = "Hello Rahul 👋, welcome to IdeaNest!"
        elif "what is ideanest" in user_message:
            ai_reply = "IdeaNest is a platform to manage, analyze, and grow startup ideas with dashboards, analytics, and AI assistance."
        elif "give some idea" in user_message:
            ai_reply = "Here are some ideas: 🚀 AI‑Powered Note App, 🌱 Smart Farming Dashboard, 🛒 E‑Commerce Clone, 🎓 Online Learning Platform, 🧳 Travel Planner."
        else:
            # fallback: cycle through default texts
            ai_reply = default_texts[len(messages) % len(default_texts)]

        messages.append({"sender": "ai", "text": ai_reply})

    return render(request, "chatbot/chat.html", {"messages": messages})
