 submit/task-update
# Task01 开发工具链与基础环境搭建
## 一、任务简介
本任务为 AI-Lab 入门基础任务，目标是完成本地开发工具链部署、终端AI Agent环境搭建、大模型API连通调试，搭建可自动化辅助编程的本地AI开发环境。

## 二、技术栈说明
- IDE：VSCode
- 运行环境：Python、Node.js
- 版本控制：Git
- API平台：SiliconFlow 硅基流动
- 初始Agent：DSH（DeepSeek Harness，自定义profile：chi）
- 备选/当前可正常运行Agent：Aider
  - Aider调用模型：DeepSeekV3
- 连通测试脚本 `api_test.py` 使用模型：Qwen/Qwen2.5-7B-Instruct

## 三、搭建过程记录
1. **初始搭建（DSH阶段）**
最初完成环境搭建，选用DSH作为CLI Agent，配置SiliconFlow密钥、chi配置文件，完成终端交互、API连通测试。
仓库内 `screenshots` 目录中 `dsh_` 开头截图，就是当时DSH环境的验收留存截图。

2. **环境故障原因**
Windows自动系统更新，重置用户环境变量，DSH的配置、运行环境失效，无法再次启动DSH。
但是当时DSH的截图文件、api_test.py脚本被保留在仓库内。

3. **备选方案验证（Aider阶段）**
为保证任务可正常验收，启用备选Agent Aider，重新配置：
- Aider对接SiliconFlow，指定调用DeepSeekV3
- 成功实现读取本地文件、新建/修改代码、执行终端命令，Agent功能验证通过
- 新增Aider交互截图存入 `screenshots` 文件夹

> 总结：DSH为最初方案，历史截图存档保留；当前可正常使用的CLI Agent为Aider，二者功能定位一致，满足任务验收要求。

## 四、各工具作用
1. VSCode：代码编辑器，管理项目、编写代码、预览Markdown
2. Git：版本控制，记录代码变更，后续提交PR评审
3. Node.js：CLI工具依赖运行环境
4. Python：运行API连通测试脚本，验证接口链路
5. DSH（初始Agent）：终端AI编程智能体（当前环境无法启动，历史留存）
6. Aider（当前可用Agent）：终端AI编程智能体，读取项目代码、辅助开发排错，通过SiliconFlow调用DeepSeekV3
7. SiliconFlow API：统一大模型调用通道，提供推理服务

## 五、交付物清单
- api_test.py 接口连通测试脚本
- README.md 任务说明文档
- screenshots/ 截图目录
  - 旧截图：dsh系列截图、环境版本截图、api代码截图、api返回结果截图
  - 新增截图：Aider终端交互成功截图
=======
# Task01：AI编程环境搭建实践报告
> 姓名：陈沁池
> 班级：数学2601
> 学号：2026002814
> 完成时间：2026-10-15

## 一、任务简介
本任务完成VS Code开发环境配置、Python虚拟环境搭建、DSH（DeepSeek Harness）网页服务部署，调用硅基流动API完成大模型交互，并且使用DSH对Python代码开展代码审查。
全部操作在太原理工大学明向校区线下完成。

## 二、开发环境信息
1. 编辑器：Visual Studio Code
2. 系统：Windows
3. Python版本：Python3.x，使用venv虚拟环境
4. 用到插件清单
- Code Runner：一键运行代码
- Error Lens：代码错误高亮提示
- GitLens：Git版本控制增强工具
- Path Intellisense：文件路径自动补全
- Prettier - Code formatter：代码格式化
- Python：Python语言基础支持
- Jupyter：Jupyter Notebook 交互支持

## 三、项目文件结构
```plaintext
Al-Lab/
├── README.md
├── api_test.py
└── screenshots/
    ├── vscode_env.jpg
    ├── dsh_terminal.jpg
    ├── api_success.jpg
    └── error_log.jpg
 
 
四、api_test.py 源代码
  
import requests

api_key = "sk-xxx"
url = "https://api.siliconflow.cn/v1/chat/completions"

payload = {
    "model": "Qwen/Qwen2.5-7B-Instruct",
    "messages": [
        {"role": "user", "content": "简单解释数列极限ε-N定义"}
    ]
}
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

res = requests.post(url, json=payload, headers=headers)
data = res.json()
print(data["choices"][0]["message"]["content"])
 
五、操作流程
 
1. 安装VS Code，在扩展市场安装任务指定全部7个插件。
2. 创建Python虚拟环境venv，激活虚拟环境。
3. 编写api_test.py，调用硅基流动的API接口。
4. 启动DSH网页端，上传代码文件，执行代码审查：逐行分析代码，识别潜在风险，给出优化建议。
5. 在PowerShell终端运行api_test.py，成功获取大模型返回文本，验证API连通。
 
六、故障排查记录（Troubleshooting）
 
问题1：VS Code提示 import "requests" could not be resolved from source
 
现象：代码中import requests出现黄色警告波浪线，无法识别库。
原因：虚拟环境内没有安装requests第三方HTTP库。
解决方法：在激活的虚拟环境终端执行安装命令
  
pip install requests
 
 
安装完成后，VS Code可以正常识别requests包，警告消失。
 
问题2：早期API调用认证失败
 
现象：调用硅基流动API返回401鉴权错误，切换多个线路均无法连通。
原因：复制API密钥时，密钥前后带有不可见空格，导致密钥无效。
解决方法：复制密钥时去除首尾空格，核对密钥完整性。
 
问题3：DSH提示 dsh-sdk 包未找到
 
现象：PowerShell出现警告 Package(s) dsh not found: dsh-sdk 
原因：当前虚拟环境没有安装dsh-sdk包，仅网页端DSH可正常使用，不影响网页端代码审查功能。
解决：如需终端使用dsh命令，执行 pip install dsh-sdk ；网页交互模式可以忽略此警告。
 
 ## 七、截图展示
VSCode插件截图
![插件截图1](screenshots/extensions_1.jpg)
![插件截图2](screenshots/extensions_2.jpg)

DSH终端启动截图
![终端npx启动DSH服务](screenshots/dsh_terminal_start.png)

DSH代码审查截图
![DSH代码审查输出结果](screenshots/dsh_code_review.png)

API调用成功截图
![终端运行api_test.py结果](screenshots/api_run_success.png)

requests报错截图
![API代码截图](screenshots/api_codeg.jpg)
 
八、收获总结
 
本次任务完成了完整的Python开发环境搭建，学会使用VS Code配套插件辅助代码编写；掌握了硅基流动API的调用方法；使用DSH完成代码审查，学会从第三方视角寻找代码漏洞。
同时在排错过程中，理解虚拟环境的作用、Python第三方包安装方法，熟悉API鉴权、密钥安全的注意事项，为后续数学建模、数据分析相关编程打下基础。
 
 master
