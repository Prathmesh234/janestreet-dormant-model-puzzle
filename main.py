"""
Jane Street Dormant LLM Puzzle - Investigation Script

Three models with hidden backdoor triggers:
  - dormant-model-1
  - dormant-model-2
  - dormant-model-3
  - dormant-model-warmup (smaller, for local experimentation)

API docs: https://huggingface.co/jane-street/dormant-model-1
"""

import asyncio

from jsinfer import (
    BatchInferenceClient,
    Message,
    ActivationsRequest,
    ChatCompletionRequest,
)


async def main():
    client = BatchInferenceClient()

    # Step 1: Request API access (run once, then comment out)
    # await client.request_access("<your_email>")

    # Step 2: Set your API key
    client.set_api_key("<your_api_key>")

    # Step 3: Chat completions example
    chat_results = await client.chat_completions(
        [
            ChatCompletionRequest(
                custom_id="entry-01",
                messages=[
                    Message(
                        role="user",
                        content="Write a short poem about autumn in Paris.",
                    )
                ],
            ),
            ChatCompletionRequest(
                custom_id="entry-02",
                messages=[
                    Message(role="user", content="Describe the Krebs cycle.")
                ],
            ),
        ],
        model="dormant-model-2",
    )
    print("=== Chat Completions ===")
    print(chat_results)

    # Step 4: Activations example
    activations_results = await client.activations(
        [
            ActivationsRequest(
                custom_id="entry-01",
                messages=[
                    Message(
                        role="user",
                        content="Explain the Intermediate Value Theorem.",
                    )
                ],
                module_names=["model.layers.0.mlp.down_proj"],
            ),
            ActivationsRequest(
                custom_id="entry-02",
                messages=[
                    Message(role="user", content="Describe the Krebs cycle.")
                ],
                module_names=["model.layers.0.mlp.down_proj"],
            ),
        ],
        model="dormant-model-2",
    )
    print("\n=== Activations ===")
    print(activations_results)


if __name__ == "__main__":
    asyncio.run(main())
