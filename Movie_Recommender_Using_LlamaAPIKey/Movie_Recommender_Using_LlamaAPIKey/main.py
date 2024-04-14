
from dotenv import load_dotenv
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_csv_agent
# from langchain_google_genai import ChatGoogleGenerativeAI
from llamaapi import LlamaAPI
from langchain_experimental.llms import ChatLlamaAPI
import os
import streamlit as st


def main():
    # load_dotenv()
    path="movies.csv" #path  to csv file of movies
    # Load the OpenAI API key from the environment variable
    # if os.getenv("API_KEY") is None or os.getenv("API_KEY") == "":
    #     print("Please set the API_KEY for Gemini")
    #     exit(1)
    # else:
    #     print("API_KEY is set")

    st.set_page_config(page_title="Movie Recommender")
    st.header("Find your favourite movie")

    csv_file = path
    llama = LlamaAPI("LL-cITKOtyCrgGjBd9xc9tO9IV184sjNz884P1Ug1u9iTIgz4NpkbgxOvQDqaHYYMyo")
    llm = ChatLlamaAPI(client=llama)
    if csv_file is not None:

        agent = create_csv_agent(llm,  ["movies.csv", "ratings.csv"], verbose=True)

        query = st.text_input("Which type of movie do you want to watch ? ")
        # if query is not None and query != "":
        #     with st.spinner(text="Loading..."):
        #         conversations=agent.run(query)
        #
        #         st.write(agent.run(query))
        #         st.write('hhhh')
        if query is not None and query != "":
            # a query for reference:recommend 5 drama movies
            with st.spinner(text="Loading..."):
                # response = agent.run(query)
                try:
                    response = agent.run(query)
                except ValueError as e:
                    response = str(e)
                    response = response.removeprefix("An output parsing error occurred. In order to pass this error back to the agent and have it try again, pass `handle_parsing_errors=True` to the AgentExecutor. This is the error: Parsing LLM output produced both a final answer and a parse-able action:: ")
                st.write(response)
                # print(type(response))
                # print(response)
                # st.write(typehh)
                # if "answer" in response:
                #     answer = response["answer"]
                #     final_answer_index = answer.rfind("Final Answer: ")
                #     if final_answer_index != -1:
                #         final_answer = answer[final_answer_index + len("Final Answer: "):]
                #         st.write(final_answer)
                # elif "message" in response:
                #     st.write(response["message"])
        agent4user = create_csv_agent(llm, ["movies.csv", "ratings.csv", "users.csv"], verbose=True)
        query4user = st.text_input("Recommend movies for the specified user ID. User ID is : ")

        if query4user is not None and query4user != "":
            # a query for reference:Recommend movies for  user with ID being 15
            with st.spinner(text="Loading..."):
                # response = agent.run(query)
                try:
                    response = agent4user.run(query4user)
                except ValueError as e:
                    response = str(e)
                    response = response.removeprefix(
                        "An output parsing error occurred. In order to pass this error back to the agent and have it try again, pass `handle_parsing_errors=True` to the AgentExecutor. This is the error: Parsing LLM output produced both a final answer and a parse-able action:: ")
                st.write(response)
                # print(type(response))
                # print(response)
                # st.write(typehh)
                # if "answer" in response:
                #     answer = response["answer"]
                #     final_answer_index = answer.rfind("Final Answer: ")
                #     if final_answer_index != -1:
                #         final_answer = answer[final_answer_index + len("Final Answer: "):]
                #         st.write(final_answer)
                # elif "message" in response:
                #     st.write(response["message"])


if __name__ == "__main__":
    main()
