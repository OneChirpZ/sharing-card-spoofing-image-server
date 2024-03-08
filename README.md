# sharing-card-spoofing-image-server

使用 Flask 写的一个简易图片服务器，同时会记录图片 GET 请求的源 IP、User agent 等信息。

## 运行方法

- 启动图片服务器
    1. python 环境：安装 requests 和 flask 库
    2. 直接运行本仓库根目录下的 `server.py`，也可将本目录作为一个 python 网站项目通过宝塔的 “网站” 功能进行部署
- 启动一个修改了 OG 协议信息的网站

## 说明

- 关于图片服务器
    - 图片服务器的本地端口号设置为了 12315，可自行修改
    - 图片位于仓库根目录下的 image 文件夹中，建议不要添加尺寸或文件大小过大的图片
    - 向服务器发送对 `http://serverIP.or.domain.name/image/filename.jpg`  的 GET 请求即可
- 钓鱼网站示例
    - 本仓库根目录下的压缩包为一个钓鱼网站的示例代码，在 `index.html` 的 `<head>` 下具有 `property="og:XXX"` 的 `<meta>` 标签声明了 OG 协议所需要的一些必要的元数据
    - 通过修改与 OG 协议相关的 `<meta>` 标签中的信息，可以变更该钓鱼网站在被 OG 协议展开时所展示的内容
        - 例如：将 `<meta property="og:image" content="http://your.server.ip.addr/image/cat.jpg">` 中的 `content` 进行修改，修改为本仓库图片服务器所提供的图片 url，即可在改变 OG 产生的网站预览图的同时，追踪预览图请求者的 IP 等信息。
- **本仓库代码仅供学术交流和学习使用，严禁用于任何非法活动。恶意利用本代码而造成的任何损失均由使用者本人负责。**