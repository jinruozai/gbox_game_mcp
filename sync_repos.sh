#!/bin/bash

# GBox Game MCP - 同步到多个远程仓库的脚本
# 使用方法: ./sync_repos.sh "提交信息"

set -e

# 检查是否提供了提交信息
if [ $# -eq 0 ]; then
    echo "❌ 请提供提交信息"
    echo "使用方法: ./sync_repos.sh \"你的提交信息\""
    exit 1
fi

COMMIT_MESSAGE="$1"

echo "🚀 开始同步 GBox Game MCP 项目..."

# 检查是否有未提交的更改
if ! git diff --quiet || ! git diff --cached --quiet; then
    echo "📝 发现未提交的更改，正在提交..."
    git add .
    git commit -m "$COMMIT_MESSAGE"
else
    echo "✅ 没有发现未提交的更改"
fi

# 推送到 GitHub
echo "📤 推送到 GitHub..."
git push origin main

# 推送到 Gitee
echo "📤 推送到 Gitee..."
git push gitee main

echo "✅ 同步完成！"
echo "🔗 GitHub: https://github.com/jinruozai/gbox_game_mcp"
echo "🔗 Gitee:  https://gitee.com/lazygoo/gbox_game_mcp" 