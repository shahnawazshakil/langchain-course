def main():
    print("Hello from langchain-course!")

    from dotenv import load_dotenv
    load_dotenv()

    from langchain_openai import ChatOpenAI
    llm = ChatOpenAI(model="gpt-4o-mini")

    print(llm.invoke("What is the capital of France?"))

if __name__ == "__main__":
    main()
