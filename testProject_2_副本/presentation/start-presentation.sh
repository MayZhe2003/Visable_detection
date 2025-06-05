#!/bin/bash

# 人车检测MCP系统演示启动脚本

echo "准备启动人车检测MCP系统演示..."

# 检查是否安装了Node.js
if ! command -v node &> /dev/null; then
    echo "错误: 未找到Node.js，请先安装Node.js"
    exit 1
fi

# 检查是否安装了npm
if ! command -v npm &> /dev/null; then
    echo "错误: 未找到npm，请先安装npm"
    exit 1
fi

# 进入演示目录
cd "$(dirname "$0")"

# 检查是否需要安装依赖
if [ ! -d "node_modules" ]; then
    echo "正在安装依赖..."
    npm install
fi

# 启动演示
echo "启动演示..."
npm run dev 