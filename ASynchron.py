import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI(
    base_url="https://<resource-name>.openai.azure.com/openai/v1/",
    api_key=token_provider,
)

async def ask(prompt):
    response = await client.responses.create(
        model="gpt-4.1",
        input=prompt
    )
    return response.output_text

async def main():
    # Issue three requests concurrently instead of one after another
    prompts = [
        "Explain quantum computing briefly.",
        "Summarize the benefits of async I/O.",
        "Give a one-sentence definition of machine learning."
    ]
    results = await asyncio.gather(*(ask(p) for p in prompts))
    for prompt, output in zip(prompts, results):
        print(f"Q: {prompt}\nA: {output}\n")

asyncio.run(main())

async def stream_response():
    stream = await client.responses.create(
        model="gpt-4.1",
        input="Write a haiku about coding.",
        stream=True
    )

    async for event in stream:
        print(event, end="", flush=True)

asyncio.run(stream_response())