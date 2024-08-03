import asyncio
import os
import dotenv

from semantic_kernel.agents.open_ai.azure_assistant_agent import AzureAssistantAgent
from semantic_kernel.contents.annotation_content import AnnotationContent
from semantic_kernel.contents.chat_message_content import ChatMessageContent
from semantic_kernel.contents.utils.author_role import AuthorRole
from semantic_kernel.kernel import Kernel

dotenv.load_dotenv(override=True)

AZURE_OPENAI_DEPLOYMENT_NAME: str = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "")
AZURE_OPENAI_ENDPOINT: str = os.getenv("AZURE_OPENAI_ENDPOINT", "")
AZURE_OPENAI_API_KEY: str = os.getenv("AZURE_OPENAI_API_KEY", "")


# A helper method to invoke the agent with the user input
async def invoke_agent(agent: AzureAssistantAgent, thread_id: str, input: str) -> None:
    await agent.add_chat_message(
        thread_id=thread_id,
        message=ChatMessageContent(role=AuthorRole.USER, content=input),
    )

    print("= " * 20, "thread", "= " * 20)
    print(f"# {AuthorRole.USER}: '{input}'")

    async for content in agent.invoke(thread_id=thread_id):
        print("- " * 20, "message", "- " * 20)
        print(f"# {content.role}: {content.content}")

        # view code when included generated code
        if len(content.items) > 0:
            for item in content.items:
                if isinstance(item, AnnotationContent) and item.file_id:
                    print("- " * 20, "generated file", "- " * 20)
                    print(f"\n`{item.quote}` => {item.file_id}")
                    response_content = await agent.client.files.content(item.file_id)
                    print(response_content.text)


async def main():

    kernel = Kernel()
    agent = AzureAssistantAgent(
        kernel=kernel,
        service_id="agent",
        name="FileManipulation",
        instructions="Find answers to the user's questions in the provided file.",
        enable_file_search=True,
        enable_code_interpreter=True,
        api_key=AZURE_OPENAI_API_KEY,
        endpoint=AZURE_OPENAI_ENDPOINT,
        deployment_name=AZURE_OPENAI_DEPLOYMENT_NAME,
        api_version="2024-05-01-preview",
    )

    await agent.create_assistant()

    csv_file_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "sample_sales_data.csv"
    )

    file_id = await agent.add_file(csv_file_path, purpose="assistants")
    thread_id = await agent.create_thread(code_interpreter_file_ids=[file_id])

    try:
        await invoke_agent(
            agent,
            thread_id=thread_id,
            input="Which category had the most sales?",
        )

    finally:
        await agent.client.files.delete(file_id)
        await agent.delete_thread(thread_id)
        await agent.delete()


if __name__ == "__main__":
    asyncio.run(main())
