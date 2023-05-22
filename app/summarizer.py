import os

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


# Got this function from this amazing course https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


def summarise_news_stories(stories):
    print("Beginning summary")
    prompt = f"""
    Your task is to generate a short summary of a series of \
    news stories given the Section, Subsection, Title and Abstract, of each story. \

    The sections are after the 'Section:'.
    The subsections are after the 'Subsection:'. The subsections can be empty.

    The title is after the 'Title:'. The abstract is after the 'Abstract:'.
    The abstract can be empty.

    Summarize the stories below, delimited by triple backticks,
    in the style of an AI trying to convey information to humans.
    Please use paragraphs where appropriate and use at most 800 words.

    Stories: ```{stories}```
    """

    return get_completion(prompt)
