def main():
    print("Hello from langchain-course!")

    from dotenv import load_dotenv
    load_dotenv()

    from langchain_openai import ChatOpenAI
    from langchain_core.prompts import PromptTemplate

    # ChatOpenAI is a ChatModel that can be used to generate text.
    # It is a wrapper around the OpenAI API.
    # ChatModel is a standart way to interact with LLMs.
    # Exmaple of ChatModels are ChatOpenAI, ChatGoogleGenerativeAI, ChatAnthropic, etc.
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.0)

    information = """
    Yosemite National Park, established in 1890 in California's Sierra Nevada mountains, 
    is a 1,200-square-mile UNESCO World Heritage site renowned for its glacial-carved valleys, 
    ancient giant sequoias, and high granite summits. Iconic landmarks include Yosemite Valley, 
    El Capitan, and Half Dome, attracting millions annually for hiking, camping, 
    and viewing world-class waterfalls.
    The 7-mile-long heart of the park, featuring towering cliffs like El 
    Capitan (a premier vertical rock climbing spot) and Half Dome.
    Known for massive spring snowmelt, featuring Yosemite Falls (one of the world's tallest at 2,425 feet), 
    Vernal Fall, Nevada Fall, and Bridalveil Fall
     Three groves of ancient, massive trees, with Mariposa Grove being the largest
    """
    summary_template = """
    You are a helpful assistant that summarizes the following information:
    {information}
    """
    # PromptTemplate is a template for a prompt.
    summary_prompt = PromptTemplate(
        template=summary_template,
        input_variables=["information"]
    )

    # Chain is a sequence of steps that are executed in order.
    # Basically it is a Runnable created using LCEL (LangChain Expression Language).
    # chain implements the full Runnable interface.
    
    summary_chain = summary_prompt | llm

    response = summary_chain.invoke({"information": information})
    
    print(response.content)
if __name__ == "__main__":
    main()
