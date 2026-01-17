from fastapi import FastAPI
from fastapi import Request
from aiModel import agent

app = FastAPI()

@app.post("/verify-news")
async def verify_news(request: Request):
    data = await request.json()
    news = data.get("news")
    response = await agent.ainvoke({"messages": [{"role": "user", "content": news}]})
   # Extract only the final AI response content
    final_answer = ""
    for msg in reversed(response["messages"]):
        if msg.type == "ai" and msg.content:
            final_answer = msg.content
            break

    return {"response": final_answer}