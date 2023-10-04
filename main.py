import google.generativeai as palm
import os

# llm initialization
key = os.getenv('google_key')

palm.configure(api_key=key)

models = [
    m for m in palm.list_models() if "generateText" in m.supported_generation_methods
]

model = models[0].name


def run_llm(prompt):
    prompt_template = f"""{prompt}"""

    completion = palm.generate_text(
        model=model,
        prompt=prompt_template,
        temperature=0,
        max_output_tokens=1024,
    )

    result = completion.result
    return result
