import gradio as gr
import openai

# Set your OpenAI API key
openai.api_key = 'api-key'
def generate_completion(user_prompt):
    hidden_context = ""
    messages = [
        {"role": "system", "content": hidden_context},
        {"role": "user", "content": user_prompt}
    ]
    response = openai.ChatCompletion.create(
        model='model_id',
        messages=messages,
        max_tokens=100,
        temperature=0
    )
    return response['choices'][0]['message']['content']

iface = gr.Interface(fn=generate_completion, inputs="text", outputs="text", title="Completion Generator")
iface.launch(share=True)
