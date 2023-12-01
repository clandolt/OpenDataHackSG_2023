from jsons import json_value, json_schema

import os
import openai
from llama_index.indices.service_context import ServiceContext
from llama_index.prompts.prompts import SimpleInputPrompt
from llama_index.llms import HuggingFaceLLM
from llama_index.indices.struct_store import JSONQueryEngine



# system_prompt = """<|SYSTEM|># StableLM Tuned (Alpha version)
# - StableLM is a helpful and harmless open-source AI language model developed by StabilityAI.
# - StableLM is excited to be able to help the user, but will refuse to do anything that could be considered harmful to the user.
# - StableLM is more than just an information source, StableLM is also able to write poetry, short stories, and make jokes.
# - StableLM will refuse to participate in anything that could harm a human.
# """

# # This will wrap the default prompts that are internal to llama-index
# query_wrapper_prompt = SimpleInputPrompt("<|USER|>{query_str}<|ASSISTANT|>")


llm = HuggingFaceLLM(
    # context_window=4096,
    # generate_kwargs={"temperature": 0.7, "do_sample": True},
    # system_prompt=system_prompt,
    # query_wrapper_prompt=query_wrapper_prompt,
    # tokenizer_name="StabilityAI/stablelm-tuned-alpha-3b",
    # model_name="StabilityAI/stablelm-tuned-alpha-3b",
    # device_map="auto",
    # stopping_ids=[50278, 50279, 50277, 1, 0],
    # tokenizer_kwargs={"max_length": 4096},
    # uncomment this if using CUDA to reduce memory usage
    # model_kwargs={"torch_dtype": torch.float16}
)

service_context = ServiceContext.from_defaults(chunk_size=1024, llm=llm, embed_model="local")

nl_query_engine = JSONQueryEngine(
    json_value=json_value,
    json_schema=json_schema,
    service_context=service_context,
)

nl_response = nl_query_engine.query(
    "How old is Anna?",
)

print(nl_response)

# raw_query_engine = JSONQueryEngine(
#     json_value=json_value,
#     json_schema=json_schema,
#     service_context=service_context,
#     synthesize_response=False,
# )
