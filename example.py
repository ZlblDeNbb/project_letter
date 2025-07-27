from prompt import API_LLM, DB_LLM, PromptMessage
from exceptions import API_Connection_Error



def ExampleMessage(api:dict, changes: str, document: str) -> str:
    sess = API_LLM(api["base_url"], api["api_llm"])
    llm = sess.connect_llm()
    mess = PromptMessage(llm, changes, document)
    response = mess.get_message()
    return response

def ExampleDBLLM_Use(llm = None):
    DataBase = DB_LLM()
    if llm != None:
        DataBase.db_append(llm)
    return DataBase.db_get() 

api = {"base_url": "https://api.vsegpt.ru/v1", "api_llm": "sk-or-vv-1a8dfaf4540f762b6c3297bda76e35360f21132ede51920cebc10796f1d6ccab"}
sess = API_LLM(api["base_url"], api["api_llm"])
# # llm = sess.connect_llm
# # llm.invoke
# change = "Претензия между ООО 'Цветочек' и ООО 'НПХ'"
# doc = "Претензия"
# ExampleMessage(api, change, doc)
base = ExampleDBLLM_Use(sess)
new_sess = base[0].connect_llm()
print(new_sess.invoke("Hi").content)
