from transformers import BertTokenizer, BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pymongo

# Load the pre-trained model and tokenizer
model_name = 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)

# Define your Query Prompt and list of keys
def get_json_data_from_mongodb():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["open_data_hack_2023"]  # Replace with your database name
    collection = db["data_hack_2023"]  # Replace with your collection name

    # Fetching the entire document
    data = collection.find_one({}, {"_id": 0})  # Fetching one document

    client.close()
    return data if data else None

list_of_strings = [f"{key}: {value}" if not isinstance(value, list) else f"{key}: {', '.join(value)}" for key, value in get_json_data_from_mongodb().items()]
print(list_of_strings)
query_prompt = "How old is John:"
keys = list_of_strings  # List of keys you want to compare

# Encode Query Prompt
encoded_query = tokenizer.encode_plus(
    query_prompt,
    add_special_tokens=True,
    return_tensors="pt"
)

# Encode keys
encoded_keys = tokenizer.batch_encode_plus(
    keys,
    add_special_tokens=True,
    return_tensors="pt",
    padding=True,
    truncation=True,
    max_length=32  # Adjust the max length as needed
)

# Ensure input tensors are in the correct shape
query_input_ids = encoded_query["input_ids"]
query_attention_mask = encoded_query["attention_mask"]

keys_input_ids = encoded_keys["input_ids"]
keys_attention_mask = encoded_keys["attention_mask"]

# Get the embeddings for Query Prompt and keys
with torch.no_grad():
    query_outputs = model(input_ids=query_input_ids, attention_mask=query_attention_mask)
    query_embedding = query_outputs.last_hidden_state[:, 0, :].numpy()

    keys_outputs = model(input_ids=keys_input_ids, attention_mask=keys_attention_mask)
    key_embeddings = keys_outputs.last_hidden_state[:, 0, :].numpy()

# Calculate cosine similarity
similarities = cosine_similarity(query_embedding, key_embeddings)

# Get the index of the maximum similarity
max_sim_index = np.argmax(similarities)

# Retrieve the element from the keys list at the max similarity index
max_similar_key = keys[max_sim_index]

# Print or use the most similar key
print("Most similar key:", max_similar_key)
print(similarities)
