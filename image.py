from openai import OpenAI
import base64

MODEL="meta-llama/Llama-3.2-11B-Vision-Instruct"
IMAGE_PATH="/mnt/d/repos/thalabus/AIServerWeb/wwwroot/images/animals/squirrel1.jpg"
BASE_URL="https://hedmlqljn2exux-3000.proxy.runpod.net/v1"

client = OpenAI(base_url=BASE_URL, api_key="dummy")
# model_list = client.models.list()
# print(model_list)

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
base64_image = encode_image(IMAGE_PATH)

def call_model():
    messages = [
            {"role": "system", "content": "You are a helpful assistant that responds in Markdown. Help me with my math homework!"},
            {"role": "user", "content": "Calculate 3+5"}
        ]
    print("Sending question to the LLM...")
    response = client.chat.completions.create(
        messages=messages,
        model=MODEL
    )
    print("...complete.")

    print(response.choices[0].message.content)

def call_model_for_image():
    print("Sending image to the LLM...")
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant that responds in Markdown. Help me with my math homework!"},
            {"role": "user", "content": [
                {"type": "text", "text": "Describe what you see in this picture"},
                {"type": "image_url", "image_url": { "url": f"data:image/png;base64,{base64_image}" } }
            ]}
        ],
        temperature=0.1,
        model=MODEL
    )
    print("...complete.")

    print(response.choices[0].message.content)

call_model()