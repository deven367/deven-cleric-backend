import json

import nltk
import requests
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from nltk import sent_tokenize

from ask_gpt4 import send_message
from responses import GetQuestionAndFactsResponse, SubmitQuestionAndDocumentsResponse

nltk.download("punkt")
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8501",
    "https://huggingface.co/spaces/deven367/frontend",
    "https://crc-assignment-validator-n65rz53nomn.streamlit.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @router.post("/submit_question_and_documents/")
# def response(payload: SubmitQuestionAndDocumentsResponse):
#     print(payload)


@app.get("/")
def read_root():
    return {"Hello": "World"}


def process_payload(payload):
    # print(dir(payload))
    print(payload)
    all_logs = payload["documents"]
    text = ""
    for log in all_logs:
        text += requests.get(log).text

    payload["text"] = text
    return payload


@app.post("/submit_question_and_documents/")
def response(payload: SubmitQuestionAndDocumentsResponse):
    # payload = json.loads(payload)
    # print(payload)
    payload = payload.model_dump()
    print(payload)
    payload = process_payload(payload)
    with open("data.json", "w") as out_file:
        json.dump(payload, out_file)
    print(payload.keys())
    return payload


@app.get("/get_question_and_facts/")
def get_question_and_facts() -> GetQuestionAndFactsResponse:
    with open("data.json", "r") as in_file:
        payload = json.load(in_file)

    print(payload.keys())
    message_log = [
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        }
    ]

    user_input = payload["question"] + payload["text"]
    message_log.append({"role": "user", "content": user_input})

    facts = send_message(message_log)
    # print(type(facts))

    response = {
        "question": payload["question"],
        "facts": sent_tokenize(facts),
        "status": "done",
    }
    return GetQuestionAndFactsResponse(**response)
