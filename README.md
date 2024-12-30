# 先锋网络中心硬件部网站

这是一个展示先锋网络中心硬件部服务和信息的网站，包含工作展示、活动介绍、组织介绍和预约表功能。

## 环境要求

- Python 3.9
- Conda

## 安装步骤

1. 克隆项目仓库：
   ```bash
   git clone https://github.com/your-repo/hardware-website.git
   cd hardware-website
   ```

2. 创建并激活Conda环境：
   ```bash
   conda create -n hardware-website python=3.9
   conda activate hardware-website
   ```

3. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

## 运行方法

1. 激活Conda环境：
   ```bash
   conda activate hardware-website
   ```

2. 启动Flask开发服务器：
   ```bash
   flask run
   ```

3. 在浏览器中访问：
   ```
   http://127.0.0.1:5000
   ```

## 项目结构

```
hardware-website/
├── app.py                # Flask应用入口
├── requirements.txt      # 依赖文件
├── static/               # 静态文件
│   └── styles.css        # 样式表
├── templates/            # HTML模板
│   ├── index.html        # 首页
│   ├── services.html     # 服务页面
│   ├── about.html        # 关于我们页面
│   └── appointment.html  # 预约页面
└── README.md             # 项目说明文件
```

## 注意事项

- 这是一个开发环境，不要在生产环境中使用
- 如需部署到生产环境，请使用WSGI服务器如Gunicorn
