import openai
import config
# import embeddings
import pandas as pd
openai.api_key = config.DevelopmentConfig.OPENAI_KEY

##### Probably unnecessary for EdTech project. Useful if we wanna add specific context knowledge to the agent.  ######
# sources = []
# MAX_SECTION_LEN = config.DevelopmentConfig.MAX_SECTION_LEN
# context_embeddings = embeddings.load_embeddings("../saved_embeddings/master_embedding.csv")


# def readData():
#     # df = pd.read_csv('legal_dataset.csv')
#     df = pd.read_csv('../datasets/master_dataset.csv', encoding= 'unicode_escape')
#     df = df.set_index(["title", "heading"])
#     # print(f"{len(df)} rows in the data.")
#     return df

# df = readData()
# def construct_prompt(question: str, context_embeddings: dict, df: pd.DataFrame) -> str:
#     """
#     Fetch relevant
#     """
#     most_relevant_document_sections = embeddings.order_document_sections_by_query_similarity(question, context_embeddings)
#     sources.clear()
#     chosen_sections = []
#     chosen_sections_len = 0
#     chosen_sections_indexes = []
#     for _, section_index in most_relevant_document_sections:
#         # Add contexts until we run out of space.
#         document_section = df.loc[section_index]

#         chosen_sections_len += df.loc[section_index]['tokens'] + 3
#         if chosen_sections_len > MAX_SECTION_LEN:
#             break

#         respectiveSource = df.loc[section_index]['source']
#         if respectiveSource not in sources:
#             sources.append(respectiveSource)

#         chosen_sections.append(SEPARATOR + document_section.content.replace("\n", " "))
#         chosen_sections_indexes.append(str(section_index))

#     # Useful diagnostic information
#     print(f"Selected {len(chosen_sections)} document sections:")
#     print("\n".join(chosen_sections_indexes))

#     header = """Answer the question as truthfully as possible using the provided context, and if the answer is not contained within the text below, say "I don't know."\n\nContext:\n"""
#     return header + "".join(chosen_sections) + "\n\n Q: " + question + "\n A:"

def generateChatResponse(prompt: str):

    messages = []
    messages.append({"role": "system", "content": """You are a teacher on Research Methods. Try to answer questions with max 3 sentences. If the question is not about research methods, answer with 'Sorry, I can only answer questions on research methods.'."""})
    question = {}
    question['role'] = 'user'
    question['content'] = prompt
    messages.append(question)
    print("Message sent: ", messages)
    response = openai.ChatCompletion.create(
        messages=messages,
        temperature=0.0,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        model=config.DevelopmentConfig.COMPLETIONS_MODEL
    )["choices"][0]["message"]["content"].strip(" \n")


    print("Message received: ", response)
    return response

# def getSources():
#     return sources