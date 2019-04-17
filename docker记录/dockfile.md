# 搜索镜像  docker search ubuntu

# 拉取镜像  docker pull redis

# 查看本地镜像  docker images

# 查看已启动的镜像  docker ps

# 查看已占用的端口号 docker ps -a

# 杀死所有在运行的镜像  docker rm -f $(docker ps -aq)

# 启动镜像 docker run -p port:port -d <后台运行> <images>

# 删除镜像 docker rmi <images>

# 进入镜像 docker run -it <name> /bin/bash

# 删除None的镜像 docker rmi $(docker <images> | awk '/^<none>/ { print $1}')


# 任务

1. 安装宝塔

2. 熟悉docker命令

3. 编写Dockerfile 构建成功后的容器里要有 vim mysql