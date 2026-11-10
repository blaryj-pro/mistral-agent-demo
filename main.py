import asyncio
from pydantic import BaseModel
import mistralai.agents as agents


class GetWeatherInput(BaseModel):
    city: str


@agents.tool(
    name="get_weather",
    description="Weather for a city.",
    input_schema=GetWeatherInput,
)
async def get_weather(args: GetWeatherInput) -> dict[str, str]:
    return {"weather": f"sunny in {args.city}"}


agent = agents.Agent(
    model="mistral-large-4",
    name="hello-agent",
    instructions="You are a friendly agent. Tell us the weather in a city.",
    tools=[get_weather],
)


async def main() -> None:
    result = await agent.run("Tell me about the weather in Paris")
    print(result.text)


if __name__ == "__main__":
    asyncio.run(main())
