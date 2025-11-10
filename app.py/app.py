from flask import Flask, request, jsonify

from flask_cors import CORS

app = Flask(__name__)

CORS(app)

# --- FAQ RESPONSES ---

faq_responses = {

    "hello": "Hi! I’m Tera — your Teralec assistant 🚀 How can I help you today?",

    "hi": "Hi! I’m Tera — your Teralec assistant 🚀 How can I help you today?",

    "contact": "You can reach our team at https://www.teralec.co.za/contact or call 073 726 7147.",

    "address": "We’re based in South Africa — you can find us here: https://www.teralec.co.za/contact.",

    "price": "Prices depend on the product or drive size — could you please tell me which item you’re interested in?",

    "hours": "We’re open Monday to Friday, 8:00 AM to 5:00 PM.",

    "thanks": "You’re very welcome 😊 Anything else I can help with?",

    "bye": "Goodbye! Have a great day 👋"

}

# --- SIMPLE MATCH FUNCTION ---

def match_faq(user_input):

    text = user_input.lower()

    for keyword, reply in faq_responses.items():

        if keyword in text:

            return reply

    return None

# --- FALLBACK MESSAGE ---

def fallback_response():

    return "Oops! You made me short circuit 😅 Please contact our team here: https://www.teralec.co.za/contact or call 073 726 7147."

# --- CHAT ROUTE ---

@app.route("/chat", methods=["POST"])

def chat():

    user_message = request.json.get("message", "")

    faq_reply = match_faq(user_message)

    if faq_reply:

        return jsonify({"reply": faq_reply, "source": "faq"})

    return jsonify({"reply": fallback_response(), "source": "fallback"})

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
Contact – TERALEC
 
