from jsons import json_value, json_schema

import os
import openai
from llama_index.indices.service_context import ServiceContext
from llama_index.llms import OpenAI
from llama_index.indices.struct_store import JSONQueryEngine


os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = os.environ["OPENAI_API_KEY"]

llm = OpenAI(model="gpt-3.5-turbo")
service_context = ServiceContext.from_defaults(llm=llm)
nl_query_engine = JSONQueryEngine(
    json_value=json_value,
    json_schema=json_schema,
    service_context=service_context,
)
raw_query_engine = JSONQueryEngine(
    json_value=json_value,
    json_schema=json_schema,
    service_context=service_context,
    synthesize_response=False,
)

nl_response = nl_query_engine.query(
    "How old is Anna Smith?",
)
raw_response = raw_query_engine.query(
    "How old is Anna Smith?",
)

print(nl_response)
