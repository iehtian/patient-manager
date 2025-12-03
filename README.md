项目说明

这是一个前后端分离的患者管理示例项目：
- 前端：Vue 3 + Vite（默认端口 `5173`）
- 后端：FastAPI + Uvicorn（建议端口 `8000`）
- 数据库：MySQL（通过 Docker 运行，容器端口 `3306`，宿主机映射到 `3307`）

目录结构（节选）
- `src/`：前端源码
- `backend/`：后端源码（`server.py`、`mysql_server.py` 等）
- `docker-compose.yml`：数据库服务编排

环境准备
- Node.js `>= 18`
- Python `>= 3.12`（与 `pyproject.toml` 要求一致）
- Docker 与 Docker Compose

数据库启动（Docker MySQL）
1. 启动容器：
	```bash
	docker compose up -d
	```
2. 连接信息（来自 `docker-compose.yml`）：
	- Host: `localhost`
	- Port: `3307` -> 容器内 `3306`
	- Database: `painter`
	- User: `painter_user`
	- Password: `painter_pass`
	- Root Password: `iehtian`
3. 首次启动会在 `painter-db-data` 卷中持久化数据。

后端启动（FastAPI + Uvicorn，使用 uv）
1. 同步依赖（基于 `pyproject.toml` 与 `uv.lock`）：
	```bash
	# 安装或更新到锁定版本
	./uv sync
	```
2. 运行开发服务（两种方式，任选其一）：
	```bash
	# 方式 A：使用 uvicorn 直接运行（推荐，支持热重载）
	./uv run uvicorn backend.server:app --host 0.0.0.0 --port 8000 --reload

	# 方式 B：使用 fastapi-cli（已在依赖中），自动检测并热重载
	./uv run fastapi dev backend/server.py --host 0.0.0.0 --port 8000
	```

前端启动（Vue 3 + Vite）
1. 安装依赖：
	```bash
	npm install
	```
2. 启动开发服务器：
	```bash
	npm run dev
	```
3. 默认访问：`http://localhost:5173`

环境变量与配置建议
- 如果 `backend/mysql_server.py` 需要从环境读取连接配置，建议在项目根目录创建 `.env`（或通过系统环境变量设置）：
  ```bash
  # 示例（与 docker-compose 保持一致）
  MYSQL_HOST=localhost
  MYSQL_PORT=3307
  MYSQL_DB=painter
  MYSQL_USER=painter_user
  MYSQL_PASSWORD=painter_pass
  ```
- 前端如需调用后端接口，建议在代码或 `.env` 中统一配置：
  ```bash
  VITE_API_BASE=http://localhost:8000
  ```

常见问题
- 无法连接数据库：确认 Docker 容器已启动，端口映射为 `3307:3306`，并使用上述凭据连接。
- CORS 报错：确保前端运行在 `http://localhost:5173`，后端已启动且允许该来源；如端口或域名不同，请在 `backend/server.py` 中调整 `allow_origins`。
- 依赖安装失败：优先升级包管理器（`pip install -U pip` 或使用 `./uv`）。

开发与调试建议
- 后端开发使用 `--reload` 自动重载；前端使用 Vite 热更新。
- 数据库初始化或示例数据可在 `backend/mysql_server.py` 中添加初始化逻辑，或使用 SQL 客户端连接到 `localhost:3307` 执行建表与插入脚本。

License
- 见项目根目录 `LICENSE`