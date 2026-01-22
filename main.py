from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
load_dotenv()


def main():
    print("Hello from langchain-course!")
    information = """Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a businessman and entrepreneur known for his leadership of Tesla, SpaceX, Twitter, and xAI. Musk has been the wealthiest person in the world since 2021; as of December 2025, Forbes estimates his net worth to be around US$779 billion.
Born into a wealthy family in Pretoria, South Africa, Musk emigrated in 1989 to Canada; he has Canadian citizenship since his mother was born there. He received bachelor's degrees in 1997 from the University of Pennsylvania in Philadelphia, United States, before moving to California to pursue business ventures. In 1995, Musk co-founded the software company Zip2. Following its sale in 1999, he co-founded X.com, an online payment company that later merged to form PayPal, which was acquired by eBay in 2002. Musk also became an American citizen in 2002."""
    summary_template = """
    given the following information {information}
    return a summary of the information in 100 words or less
    """
    summary_prompt = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    chain = summary_prompt | llm
    result = chain.invoke({"information": information})
    print(result.content)


if __name__ == "__main__":
    main()
