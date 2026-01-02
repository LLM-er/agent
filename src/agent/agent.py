# import os
# from typing import Literal
# from tavily import TavilyClient
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_community.utilities import SearxSearchWrapper
from langchain_community.tools import SearxSearchResults

print("aiduo agent start ....")

# # 1. 先创建 SearxSearchWrapper
search_wrapper = SearxSearchWrapper(
    searx_host="http://aiduo.chat:8080",  # 你的 SearxNG 地址
    engines=["sogou", "bing"],              # 可选：搜索引擎列表
)

# 2. 再创建工具，传入 wrapper
internet_search = SearxSearchResults(
    wrapper=search_wrapper,
    name="internet_search",                   # 工具名称
    description="aiduo.chat 搜索引擎",
    num_results=9,                           # 返回结果数量
)

# 直接调用工具测试
# results = searxng_tool.invoke({"query": "Python LangChain"})
# print(results)

llm = init_chat_model(
    model="deepseek-chat",      # 或 "deepseek-coder"
    model_provider="deepseek",  # 指定 DeepSeek 提供商
    api_key="sk-315fd883a269474098dae7819343ee94",
    # temperature=0.7,
)

# 测试
# response = llm.invoke("你好，介绍一下 LangChain")
# print(response.content)

# tavily_client = TavilyClient(api_key="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")

# def internet_search(
#     query: str,
#     max_results: int = 5,
#     topic: Literal["general", "news", "finance"] = "general",
#     include_raw_content: bool = False,
# ):
#     """Run a web search"""
#     return tavily_client.search(
#         query,
#         max_results=max_results,
#         include_raw_content=include_raw_content,
#         topic=topic,
#     )

# qres = tavily_client.search("重庆天气")
# print("qres", qres)

# System prompt to steer the agent to be an expert researcher
research_instructions = """You are an expert researcher. Your job is to conduct thorough research and then write a polished report.

You have access to an internet search tool as your primary means of gathering information.

## `internet_search`

Use this to run an internet search for a given query. You can specify the max number of results to return, the topic, and whether raw content should be included.
"""

agent = create_agent(
    model=llm,
    tools=[internet_search],
    system_prompt=research_instructions
)

# result = agent.invoke({"messages": [{"role": "user", "content": "讲讲重庆的特色"}]})
# print(result["messages"][-1].content)