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
