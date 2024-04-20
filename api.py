from fastapi import APIRouter, FastAPI

from ask_gpt4 import send_message
from responses import GetQuestionAndFactsResponse, SubmitQuestionAndDocumentsResponse

app = FastAPI()


# @router.post("/submit_question_and_documents/")
# def response(payload: SubmitQuestionAndDocumentsResponse):
#     print(payload)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/submit_question_and_documents/")
def response(payload: SubmitQuestionAndDocumentsResponse) -> GetQuestionAndFactsResponse:
    payload = payload.model_dump()
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
        "facts": facts.split("\n"),
        "status": "success",
    }
    return GetQuestionAndFactsResponse(**response)


# app.include_router(router)
