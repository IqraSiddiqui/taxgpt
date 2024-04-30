from django.shortcuts import render
from django.http import JsonResponse
from ..models import W2Data
import requests
from rest_framework import generics
import sqlite3
from typing import List
import pandas as pd
import g4f
from langchain.llms.base import LLM
from typing import Optional, List
from langchain.sql_database import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import PromptTemplate
import json
from django.db import connection



class SQLQuery:
    def __init__(self, sql_database: str):
        self.connection = sqlite3.connect(sql_database, check_same_thread=False)

    def run(self, queries: List[str]) -> dict:
        results = []
        for query in queries:
            result = pd.read_sql(query, self.connection)
            results.append(result)
        return {"results": results, "queries": queries}

class customLLM(LLM):
  @property
  def _llm_type(self)->str:
    return "custom"
  def _call(self,prompt:str, stop: Optional[List[str]]=None)->str:
    out=g4f.ChatCompletion.create(model=g4f.models.gpt_35_turbo, messages=[{"role": "user", "content": prompt}])
    return out

class ChatView(generics.GenericAPIView):
    sql_query = SQLQuery('db.sqlite3')

    def process_prompt(self,prompt):
        Template="""You are a {dialect} expert. Given an input question,first create a syntactically correct {dialect} query to run,then execute the query and return the answer.

        Use the following multidimensional fact tables:

        {table_info}

        The table W2Data contains the W2 form information regarding tax.
        It includes the following columns:
        Employee_SSA_number: SSA number of employee as text that you will use to filter database.
        Employee_address: address of the employee.
        Employer_FED_ID: FED ID of the employer as text.
        Employer's name: name of the employer.
        Employee's name: name of the employee.
        Social_Security: amount of social security paid.
        Gross_Pay: gross pay amount.
        Local_income_tax: local income tax amount paid.
        State_income_tax: state income tax amount paid.
        Medicare_tax: medicare tax amount paid.
        State_employer_state_id: state id of the state employer as integer.
        State_wages: wages by the state.
        Tax_withheld: withholding tax amount.


        Use the following format:

        Question: Question here
        SQLQuery: SQL Queries to run

        Question: {input}
        """


        PROMPT = PromptTemplate(
                input_variables=["input", "table_info", "dialect"], template=Template
            )

        db = SQLDatabase.from_uri('sqlite:///W2_data.db')
        llm = customLLM()

        sql_chain = SQLDatabaseChain.from_llm(
                llm=llm,
                db=db,
                prompt=PROMPT,
                return_sql=False,
                verbose=True  # Adjust verbosity as needed
            )
        ans=sql_chain.run(prompt)
        return ans

    def post(self, request):
        try:
            data = json.loads(request.body.decode('utf-8'))
            prompt = data.get('prompt')
            if prompt:
                # Process the prompt (e.g., generate response)
                response = self.process_prompt(prompt)
                print(response)
                return JsonResponse({'response': response})
            else:
                return JsonResponse({'error': 'Prompt not found'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)