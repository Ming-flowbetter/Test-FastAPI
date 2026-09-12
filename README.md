# My First AI Agent API

这是一个从零学习 FastAPI 和 AI Agent 的练习项目。

## 本地运行

在项目根目录打开 PowerShell：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

然后打开 <http://127.0.0.1:8000/docs> 测试 API。

## 部署到 Render

将项目推送到 GitHub 后，在 Render 中创建 Web Service，选择这个仓库。
项目中的 `render.yaml` 已经配置了构建和启动命令。部署成功后，可以访问：

```text
https://你的服务名.onrender.com/docs
```
