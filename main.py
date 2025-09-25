import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_propositions(text):
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError(
            "Falta la API key de OpenRouter en el .env (OPENROUTER_API_KEY)"
        )

    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "https://openrouter.ai/",
        "Content-Type": "application/json",
    }

    data = {
        "model": "openai/gpt-3.5-turbo",  # You can also try other models like "mistralai/mistral-7b-instruct"
        "messages": [
            {
                "role": "system",
                "content": "You are an expert in propositional logic in Spanish.",
            },
            {
                "role": "user",
                "content": (
                    "Identify the propositions in the following Spanish paragraph, assign a letter to each proposition, and "
                    "return the resulting propositional function using logical operators "
                    "(such as ∧, ∨, ¬, →, ↔).\n\n"
                    "Example input:\n"
                    "Si tuvieran que justificarse ciertos hechos por su enorme tradición entonces, si estos hechos son "
                    "inofensivos y respetan a todo ser viviente y al medio ambiente, no habría ningún problema. Pero si los "
                    "hechos son bárbaros o no respetuosos con los seres vivientes o el medio ambiente, entonces habría que "
                    "dejar de justificarlos o no podríamos considerarnos dignos de nuestro tiempo.\n\n"
                    "Example output:\n"
                    "p: justificar hechos por su tradición.\n"
                    "q: ser inofensivo.\n"
                    "r: ser respetuoso con los seres vivos.\n"
                    "s: ser respetuoso con el medio ambiente.\n"
                    "t: tener problemas.\n"
                    "¬q: ser bárbaro (= no ser inofensivo).\n"
                    "u: ser digno de nuestro tiempo.\n\n"
                    "Propositional function:\n"
                    "(p → ((q ∧ r ∧ s) → ¬t)) ∧ ((¬q ∨ ¬r ∨ ¬s) → (¬p ∨ ¬u))\n\n"
                    "Input:\n"
                    f"{text}\n\n"
                ),
            },
        ],
    }


    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]


if __name__ == "__main__":
    paragraph = input("Introduce el párrafo: ")
    result = get_propositions(paragraph)
    print(result)
