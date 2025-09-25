# Propositions Detector

A Python tool that uses AI to identify propositions in Spanish text and convert them into propositional logic functions using logical operators.

## Features

- **Proposition Detection**: Automatically identifies logical propositions in Spanish text
- **Letter Assignment**: Assigns variables (p, q, r, s, etc.) to each proposition
- **Logical Function Generation**: Creates formal propositional logic expressions
- **AI-Powered**: Uses OpenRouter API with GPT-3.5-turbo for intelligent text analysis

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/N3VERS4YDIE/propositions-ai-detector.git
   cd propositions-ai-detector
   ```

2. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:

   - On Linux/macOS:

      ```bash
      source .venv/bin/activate
      ```
  
   - On Windows:

      ```bash
      .venv\Scripts\activate
      ```

4. Install required dependencies:

   ```bash
   pip install requests python-dotenv
   ```

5. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Add your OpenRouter API key to the `.env` file:

   ```bash
   OPENROUTER_API_KEY=your_api_key_here
   ```

## Usage

Run the main script:

```bash
python main.py
```

Enter a Spanish paragraph when prompted, and the tool will return:

- Identified propositions with assigned letters
- The resulting propositional logic function

### Example

**Input:**

```txt
Si tuvieran que justificarse ciertos hechos por su enorme tradición entonces, si estos hechos son inofensivos y respetan a todo ser viviente y al medio ambiente, no habría ningún problema. Pero si los hechos son bárbaros o no respetuosos con los seres vivientes o el medio ambiente, entonces habría que dejar de justificarlos o no podríamos considerarnos dignos de nuestro tiempo.
```

**Output:**

```txt
p: justificar hechos por su tradición.
q: ser inofensivo.
r: ser respetuoso con los seres vivos.
s: ser respetuoso con el medio ambiente.
t: tener problemas.
¬q: ser bárbaro (= no ser inofensivo).
u: ser digno de nuestro tiempo.

Propositional function:
(p → ((q ∧ r ∧ s) → ¬t)) ∧ ((¬q ∨ ¬r ∨ ¬s) → (¬p ∨ ¬u))
```

## API Configuration

This project uses OpenRouter API to access GPT-3.5-turbo. You can also modify the model in `main.py` to use other available models.

To get an OpenRouter API key:

1. Visit [OpenRouter](https://openrouter.ai/)
2. Create an account
3. Generate an API key
4. Add it to your `.env` file

## Project Structure

```bash
propositions-ai-detector/
│
├── main.py         # Main application script
├── .env.example    # Environment variables template
├── .env            # Environment variables (not tracked)
├── .gitignore      # Git ignore rules
├── .venv/          # Virtual environment (not tracked)
└── README.md       # This file
```

## License

This project is open source and available under the [MIT License](LICENSE).
