from openai import OpenAI

client = OpenAI()


def get_ai_financial_brief(text):
    prompt = f"""
You are a financial research assistant.

Analyze the following text and provide:

--- SUMMARY ---
(2-3 sentences)

--- KEY INSIGHTS ---
(2-4 bullet points)

--- RISKS ---
(2-3 bullet points)

--- OPPORTUNITIES ---
(2-3 bullet points)

--- FINAL TAKEAWAY ---
(1-2 sentences)

Keep the tone professional, concise, and analytical.

Text:
{text}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text


def main():
    user_input = input("Enter a company or paste text: ")
    result = get_ai_financial_brief(user_input)

    print("\n" + result)

    filename = input("\nEnter a filename to save your brief: ")
    with open(filename + ".txt", "w") as file:
        file.write(result)

    print(f"\nSaved to {filename}.txt")


if __name__ == "__main__":
    main()