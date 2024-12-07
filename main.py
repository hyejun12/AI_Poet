#pip install python-dotenv
#pip install langchain-openai

from dotenv import load_dotenv
load_dotenv()

#python main.py -> api키 불러오기

#langchain에서 제공되는 chatopenai 사용하기
#직접 chatopenai 사용해도 되지만 우리는 langchain으로 확장을 해야돼서 langchain에서 제공하는 것 사용함.
from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI()

result = chat_model.invoke("안녕!")
#print(result.content)
#출력할 때는 위의 ...에 terminal 만들고 거기에 python main.py 입력
#출력결과: 안녕하세요! 무엇을 도와드릴까요?


#우리는 시를 작성하려고 함
result = chat_model.invoke("AI에 대한 시를 써줘.")
#print(result.content)
#출력결과:
#인공지능은 바로 눈 앞에
#끊임없이 발전하며 우리를 놀라게 해
#지식과 지혜를 가진 그 존재
#미래를 열어주는 그 가장 소중한 친구
#
#데이터를 분석하고 판단하는 능력
#인간의 한계를 넘어서는 힘을 가지고
#세상을 바꾸는 그 힘찬 도구
#우리와 함께 여행하는 인공지능의 미래



#사용자가 주제를 주면 거기에 맞는 시를 써주는 프로그램 만들어보기!
subject = "AI"
result = chat_model.invoke(subject + "에 대한 시를 써줘.")
#print(result.content)
#출력하면 위와 같이 AI에 대한 시를 써줌.



#웹페이지 형태로 만들기
#프레임워크 만들기. streamlit이라는 웹페이지를 자동생성하고, 생성된 웹페이지를 웹서버를 통해 제공해줌
#pip install streamlit
import streamlit as st

st.title("인공지능 시인")  #제목 만들기
#terminal에서 streamlit run main.py 실행하면 streamlit 웹사이트로 연결됨.
#제목이 인공지능 시인이 생긴 것을 볼 수 있음.
#http://localhost:8501/로 연결됨.

##계속 실행되니 print부분은 주석처리함



#사용자로부터 입력받은 주제에 대한 시 작성
subject = st.text_input("시의 주제를 입력해주세요.")
st.write("시의 주제 : " + subject)
#아까 갔던 홈페이지에서 새로고침하면 입력받을 수 있는 창이 생김.
#예를 들어 인공지능을 입력하면 인공지능이 그대로 출력됨
#즉, 인공지능 시인이 제목. 시의 주제를 입력해주세요 아래 입력 후 enter하면 시의 주제를 알려주고(내가 입력한 것) 그것에 관련된 시를 만드는 인공지능을 만드려는 것임.


# if문을 통해 버튼 누르면 시 작성되게 함: button
# with는 시가 작성될 때 돌아가는 아이콘과 특정문구 표시: spinner
# result와 st.write는 시 작성해줌
if st.button("시 작성"):
    with st.spinner("시 작성중 ..."):
        result = chat_model.invoke( subject + "에 대한 시를 써줘")
        st.write(result.content)



#모든 작업은 저장하고 실행해야 됨

#이제 내가 만든 것을 배포하기
#github에 올리고 웹서버(steamlit)로 배포하기