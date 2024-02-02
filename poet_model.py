# from dotenv import load_dotenv
# load_dotenv()
from langchain_openai import OpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

output_parser = StrOutputParser()
llm = OpenAI()
# llm = OpenAI(openai_api_key="")
st.title('명언제조기')

content = st.text_input('키워드를 입력해주세요')

if st.button('확인'):
       
    st.write(content + '에 대한 명언을 만들겠습니다')
    with st.spinner('Wait for it...'):
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a world-class sage."),
            ("user", "{input}에 대한 명언을 한글로 만드는데 마지막 문장에는  '''명심해라, ''' 를 넣어서\
            세 문장으로 만들어서 보여주고 영어로 번역 한 후에 세문장을 합쳐서 한문장으로 다시 보여주고 번역해줘 ")
        ])


    chain = prompt | llm | output_parser

    result = chain.invoke({"input": content})

# result = llm.invoke("내가 좋아하는 동물은?")
    st.write(result)
    print(result)



