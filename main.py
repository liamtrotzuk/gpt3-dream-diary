import openai
import pandas as pd

DF_dreams = pd.read_csv(r'/Users/liamtrotzuk/Downloads/Dream Diary - main.csv')

LIST_description = DF_dreams['Description'].to_list()
LIST_dreams_last_10 = LIST_description[-10:-1]

STR_dreams_last_10 = " "
for x in LIST_dreams_last_10:
    STR_dreams_last_10 = STR_dreams_last_10 + " " + x

openai.api_key = "xx-xxxxx"
openai.Completion.create(
    model="text-davinci-002",
    prompt="Is the following list of dreams predominately positive or predominately negative or predominately neutral? How many are positive? How many are negative? How many are neutral?" + STR_dreams_last_10,
    max_tokens=2000,
    temperature=0.9)

openai.Completion.create(
    model="text-davinci-002",
    prompt="What does the following list of dreams say about the dreamer's mental state?" + STR_dreams_last_10,
    max_tokens=2000,
    temperature=0.9)

openai.Completion.create(
    model="text-davinci-002",
    prompt="What is the overarching theme of the following list of dreams?" + STR_dreams_last_10,
    max_tokens=2000,
    temperature=0.9)
