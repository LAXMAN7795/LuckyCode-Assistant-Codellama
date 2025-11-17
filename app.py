import requests
import gradio as gr
import json

url = "http://localhost:11434/api/generate"

headers = {
    "Content-Type": "application/json"
}

history = []

def generate_response(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)

    data = {
        "model": "LuckyCode",
        "prompt": final_prompt,
        "stream": False,# to get complete response at once
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        response = response.text
        data = json.loads(response)
        actual_response = data['response']
        return actual_response
    else:
        print(f"Error: {response.status_code}")# or response.text

interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=5, label="Enter your prompt"),
    outputs=gr.Textbox(lines=10, label="Response"),
    title="LuckyCode AI Assistant",
    description="Interact with the LuckyCode AI model."
)
interface.launch()