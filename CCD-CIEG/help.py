import subprocess, pkg_resources

required_version = "4.30.2"

def install_transformers(version):
    subprocess.run(f"pip install transformers=={version}", shell=True, check=True)

try:
    version = pkg_resources.get_distribution("transformers").version
    print(f"当前 transformers 版本: {version}")
    if version != required_version:
        print(f"正在安装兼容版本 transformers=={required_version} ...")
        install_transformers(required_version)
except pkg_resources.DistributionNotFound:
    print("未安装 transformers，正在安装...")
    install_transformers(required_version)

print("环境已准备好，现在可以重新运行 fewshot.py")
