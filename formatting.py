import pandas as pd

df = pd.read_csv("/home/haris/Desktop/Web Scraping/finetune/techinalupd.csv")
df.insert(0, "New Column", "")
for index, row in df.iterrows():

    user_data = row[1]
    assistant_data = row[2]
    

    user_message = '{{"role": "user", "content": "{}"}}'.format(user_data)
    assistant_message = '{{"role": "assistant", "content": "[{}]"}}'.format('"{}"'.format(assistant_data))

    final_message = '{{"messages": [{{"role": "system", "content": "Welcome to WheelsMasail! Your go-to chatbot for all things related to wheels. Ask me anything about cars, maintenance, troubleshooting, or any automotive topic. I\'m here to assist you!"}}, {}, {}]}}'.format(user_message, assistant_message)

    df.at[index, "New Column"] = final_message

df.to_csv("/home/haris/Desktop/Web Scraping/finetune/modified_file.csv", index=False)

print("Modified CSV file saved successfully as 'modified_file.csv'")
