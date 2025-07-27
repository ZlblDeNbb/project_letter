import requests

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate


class API_LLM:
    def __init__(self, base_url, api_key, model='gpt-4o-mini') -> None:
        self.base_url = base_url
        self.api_key = api_key
        self.model = model
    
    def connect_llm(self):
        """
        Подключение к LLM. Возвращает объект ChatOpenAI.
        """
        llm = ChatOpenAI(api_key=self.api_key, model=self.model,
                        base_url=self.base_url)
        return llm
    
    def test_connection(self):
        """
        Тестирует подключение к LLM по API.
        """
        try:
            response = self.connect_llm  # Для OpenAI-совместимых API
            print("Сервер доступен. Статус:", response.status_code)
            return TrueS
        except requests.exceptions.RequestException as e:
            print("Ошибка подключения к серверу:", str(e))
            return False


class DB_LLM:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls._instance = super(DB_LLM, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.__db = []
    
    def db_append(self, llm):
        """
        Добавление в базу данных LLM.
        """
        self.__db.append(llm)
    
    def db_remove(self, llm):
        """
        Удаление из базы данных LLM.
        """
        self.__db.remove(llm)
    
    def db_get(self):
        """
        Получение базы данных LLM.
        """
        return self.__db


class PromptMessage:
    def __init__(self, llm_api, changes, document):
        self.llm_api = llm_api
        self.changes = changes
        self.document = document
    
    def get_message(self):
        prompt = """Напиши документ по примеру документа приведенного в качестве примера.
        Измени в документе следующие данные:
        {changes}
        Example: {document}
        Answer: В ответе должен быть только документ, без рассуждений"""
        doc_temp = PromptTemplate(template=prompt, input_variables=["changes","document"])
        return self.llm_api.invoke(doc_temp.format(changes=self.changes, document = self.document)).content
        