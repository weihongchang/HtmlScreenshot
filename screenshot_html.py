from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

def screenshot_html_file(html_path, screenshot_path="screenshot.png", wait_seconds=10):
    """
    打开HTML文件并等待指定秒数后截图
    
    参数:
    html_path: HTML文件的路径（绝对路径/相对路径均可）
    screenshot_path: 截图保存的路径，默认是当前目录下的screenshot.png
    wait_seconds: 等待秒数，默认10秒
    """
    # 1. 处理HTML文件路径，转换为绝对路径并格式化为URL
    abs_html_path = os.path.abspath(html_path)
    file_url = f"file:///{abs_html_path}"  # 格式化为浏览器可识别的本地文件URL

    # 2. 配置Chrome浏览器选项
    chrome_options = Options()
    # 可选：无头模式（不显示浏览器窗口），如果需要看到浏览器窗口可注释这行
    chrome_options.add_argument("--headless=new")
    # 可选：设置窗口大小，保证截图完整
    chrome_options.add_argument("--window-size=1080,1920")

    try:
        # 3. 启动Chrome浏览器
        driver = webdriver.Chrome(options=chrome_options)
        
        # 4. 打开HTML文件
        print(f"正在打开HTML文件: {html_path}")
        driver.get(file_url)
        
        # 5. 等待指定秒数（让页面完全加载/渲染）
        print(f"等待 {wait_seconds} 秒...")
        time.sleep(wait_seconds)
        
        # 6. 截图并保存
        driver.save_screenshot(screenshot_path)
        print(f"截图已保存至: {os.path.abspath(screenshot_path)}")

    except FileNotFoundError:
        print(f"错误：未找到HTML文件 {html_path}")
    except Exception as e:
        print(f"执行出错：{str(e)}")
    finally:
        # 7. 确保浏览器关闭，释放资源
        if 'driver' in locals():
            driver.quit()

# 主程序入口
if __name__ == "__main__":
    # 替换为你的HTML文件路径（相对/绝对路径都可以）
    HTML_FILE_PATH = "test.html"  # 示例：当前目录下的test.html
    # 调用函数执行截图
    screenshot_html_file(HTML_FILE_PATH)