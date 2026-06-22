import google.generativeai as genai
import pandas as pd
import json
import streamlit as st

genai.configure(api_key="your_key")
model=genai.GenerativeModel("gemini-2.5-pro")

print("Chatbot is ready! Type 'exit' to stop.\n")

if "chat" not in st.session_state:
    st.session_state.chat=[]
    
user_input=st.text_input("You : ")
if(st.button("Send")):
    if(user_input):
        if user_input.lower()=="exit":
            st.session_state.chat.append({"you":"exit","Chatbot":"Good Bye"})
            st.stop()  
        else:
            response=model.generate_content(user_input)
            st.write("Chatbot : ",response.text)
            st.session_state.chat.append({"you" : user_input,"Chatbot" : response.text})
                
    else:
        st.write("waiting.......")


if st.button("Save chat"):
    with open("chat.json","w") as f1:
        b=json.dump(st.session_state.chat,f1,indent=4)    
        
        #if user_input.lower()=="exit":
         #   print("Chatbot: Goodbye!")
          #  break
        #response=model.generate_content(user_input)
        #st.write("Chatbot : ",response.text)
        #a.append({"you" : user_input,"Chatbot" : response.text})
    #b=json.dump(a,f1,indent=4)

