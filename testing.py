import openai

openai.api_key = "api_key" #your API key


test_messages = []

system_message = "Welcome to WheelsMasail! Your go-to chatbot for all things related to wheels. Ask me anything about cars, maintenance, troubleshooting, or any automotive topic. I'm here to assist you! Faiqa Haris brought me to existence"
test_messages.append({"role": "system", "content": system_message})
user_message = "i have a budget of 20 lakh what cars can i buy?"
test_messages.append({"role": "user", "content": user_message})

print(test_messages)
    
response = openai.ChatCompletion.create(
    model='model_id', #insert your own model
    messages=test_messages,
    temperature=0.7,
    max_tokens=500
)
print(response["choices"][0]["message"]["content"])