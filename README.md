# HtmlScreenshot

前置条件（必做）

安装依赖库：

bash

运行

pip install selenium

下载 ChromeDriver：

selenium 需要 ChromeDriver 来驱动 Chrome 浏览器，下载地址：https://sites.google.com/chromium.org/driver/

注意：ChromeDriver 版本需与你的 Chrome 浏览器版本匹配（可在 Chrome 的「设置 - 关于 Chrome」查看版本）

配置方式（二选一）：

将 ChromeDriver 放到系统环境变量的路径中；

在代码中指定 ChromeDriver 路径，修改 webdriver.Chrome 这一行：

python
运行
driver = webdriver.Chrome(executable_path="你的ChromeDriver路径", options=chrome_options)