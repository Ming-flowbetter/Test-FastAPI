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
