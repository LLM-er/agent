{
  "$schema": "https://langgra.ph/schema.json",
  "dependencies": ["."],
  "graphs": {
    "agent": "./src/agent/agent.py:agent"
  },
  "env": ".env",
  "runtime": {
    "max_workers": 1,              // 单线程，无 Redis
    "worker_timeout": 600          // 10分钟超时
  },
  "store": {
    "module": "inmem"              // 内存存储 (deepagents 自动使用)
  },
  "checkpointer": {
    "module": "inmem"              // 内存 checkpointer
  },
  
  "image_distro": "wolfi",         // 指定基础镜像
  "python_version": "3.12"         // docker 部署时指定的 Python 版本，会自动安装，无论服务器上是否安装

}

docker-compose -f aiduo-docker-compose.yml up -d // 运行docker配置文件

pip list | findstr langchain-community 查看已安装的包
pip show langchain-community 查看已安装的包