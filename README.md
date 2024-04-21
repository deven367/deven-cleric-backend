# deven-cleric-backend

For the backend, I have used `fastapi` and `pydantic` for data validation. The model working on the backend to give insights from the logs is GPT-4.

The OpenAI's API key is set as an environment variable in the configuration on the deployment.

## To run the backend locally

```sh
pip install -r requirement.txt
```

Once the requirements are installed, run the command

```sh
uvicorn api:app --reload
```

to run the app locally.

## Model choice

Upon some testing, I found GPT-3.5 Turbo also working reliably. However, I went GPT-4 for a safer measure. GPT-4 takes slightly longer than GPT-3.5 for receiving the response, but the quality of the reponse is better than GPT-3.5.

## Code organization and approach

The code is organized in the following way:

```md
|- api.py               # FastAPI app
|- ask_gp4.py           # GPT-4 model
|- responses.py         # Pydantic Response model
|- requirements.txt     # Requirements
```

1. The `api.py` file contains the FastAPI app, which has two endpoints `/submit_question_and_documents` which takes a `POST` request with a JSON body containing the `question` key and urls of logs.
2. The `POST` request is validated using Pydantic models. The logs are fetched from the URLs by sending a `GET` request and the question and logs are sent to the GPT-4 model.
   1. All the logs are concatenated and sent to the GPT-4 model, so that has the entire context for generating the response.
   2. Once the logs are concatenated, the processed payload is written to a file.
   3. The `GET` endpoint then reads the file, checks if the logs were fetched correctly, and if not, it returns an error. Else, it sends the payload to the GPT-4 model.
3. The `ask_gp4.py` file pings the GPT-4 endpoint, which is used to generate the response.
4. The `responses.py` file contains the Pydantic Response model, which is used to validate the response from the GPT-4 model.
