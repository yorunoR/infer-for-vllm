import litellm

litellm.set_verbose=True

model = "openai/cyberagent/calm2-7b-chat"
# model = "openai/elyza/ELYZA-japanese-Llama-2-13b-instruct"
# model = "openai/tokyotech-llm/Swallow-13b-instruct-hf"

system = "あなたは誠実で優秀な日本人のアシスタントです。"
# content = "こんにちは"
content = "仕事の熱意を取り戻すためのアイデアを5つ挙げてください。"

response = litellm.completion(
    model=model,
    api_key="EMPTY",
    api_base="http://localhost:4000/v1",
    messages=[
        {"role": "system", "content": system},
        {"role": "user", "content": content},
    ],
    max_tokens=1024,
    temperature=0.1,
    frequency_penalty=0,
    presence_penalty=-0.8
)

print(response)