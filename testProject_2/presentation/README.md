# 人车检测MCP系统演示

这是一个使用[Slidev](https://sli.dev/)创建的演示文稿，介绍基于YOLOv8的人车检测MCP系统。

## 运行演示

确保您已安装Node.js (v14+)，然后按照以下步骤操作：

```bash
# 进入演示目录
cd /Users/p/Desktop/testProject_2/presentation

# 安装依赖
npm install

# 启动演示
npm run dev
```

演示将在浏览器中自动打开，通常是在 http://localhost:3030

## 构建静态网站

如果您想将演示构建为静态网站：

```bash
npm run build
```

生成的文件将位于 `dist` 目录中。

## 导出为PDF

要导出为PDF：

```bash
npm run export
```

## 演示内容

演示文稿包括以下内容：

- 人车检测系统概述
- MCP协议介绍
- 系统架构和技术栈
- MCP工具函数说明
- Cursor中的部署方法
- 演示流程和系统功能

## 自定义

您可以编辑 `slides.md` 文件来修改演示内容。更多信息请参考 [Slidev 文档](https://sli.dev/)。 